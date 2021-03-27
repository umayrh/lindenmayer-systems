import turtle
import tkinter

from typing import Callable, List

from pathlib import Path
import tempfile
import re, os, sys, functools, subprocess, shutil

import PIL.Image
from PIL.PngImagePlugin import PngImageFile
from PIL.ImageFile import ImageFile
from PIL import EpsImagePlugin

# This code is adapted from https://stackoverflow.com/a/63369598/3113353
# For GIF compression:
#   mogrify -layers 'optimize' -fuzz 7% data/Quadratic\ Koch\ island.gif
#   convert input.gif -coalesce -scale 700x525 -fuzz 2% +dither -remap input.gif[0] -layers Optimize output.gif


def init(**options):
    # download ghostscript: https://www.ghostscript.com/download/gsdnld.html
    # install ghostscript, otherwise->{OSError} Unable to locate Ghostscript on paths
    if options.get('gs_windows_binary'):
        EpsImagePlugin.gs_windows_binary = options['gs_windows_binary']

    # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cap-join-styles.html
    # change the default style of the line that made of two connected line segments
    # default is ROUND  # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_line.html
    tkinter.ROUND = tkinter.BUTT


def make_gif(image_list: List[Path], output_path: Path, **options):
    """
    :param image_list:
    :param output_path:
    :param options:
        - fps: Frame Per Second. Duration and FPS, choose one to give.
        - duration milliseconds (= 1000/FPS )  (default is 0.1 sec)
        - loop  # int, if 0, then loop forever. Otherwise, it means the loop number.
    :return:
    """
    if not output_path.parent.exists():
        raise FileNotFoundError(output_path.parent)

    if not output_path.name.lower().endswith('.gif'):
        output_path = output_path / Path('.gif')
    image_file_list: List[ImageFile] = [PIL.Image.open(str(_)) for _ in image_list]

    im = image_file_list.pop(0)
    fps = options.get('fps', options.get('FPS', 10))
    duration = options.get('duration', int(1000 / fps))
    print(f'# images: {len(image_file_list)}, duration: {duration}')
    im.save(output_path, format='gif', save_all=True, append_images=image_file_list,
            duration=duration,
            loop=options.get('loop', 0))
    [_.close() for _ in image_file_list]


class GIFCreator:
    __slots__ = ['draw',
                 '__temp_dir', '__duration',
                 '__name', '__is_running', '__counter', ]

    BASE_PATH = '../../data'
    # The time gap that you pick image after another on the recording. i.e.,
    # If the value is low, then you can get more source image, so your GIF has higher quality.
    DURATION = 100  # millisecond.  # 1000 / FPS
    REBUILD = True

    def __init__(self, name, temp_dir: Path = None, duration: int = None, **options):
        self.__name = name
        self.__is_running = False
        self.__counter = 1

        self.__temp_dir = temp_dir if temp_dir else Path(tempfile.mkdtemp(prefix='temp_for_gifs'))
        self.__duration = duration if duration else self.DURATION

        if not self.__temp_dir.exists():
            self.__temp_dir.mkdir(parents=True)  # True, it's ok when parents is not exists

    @property
    def name(self):
        return self.__name

    @property
    def duration(self):
        return self.__duration

    @property
    def temp_dir(self):
        if not self.__temp_dir.exists():
            raise FileNotFoundError(self.__temp_dir)
        return self.__temp_dir

    def configure(self, **options):
        gif_class_members = (_ for _ in dir(GIFCreator)
                             if not _.startswith('_') and not callable(getattr(GIFCreator, _)))

        for name, value in options.items():
            name = name.upper()
            if name not in gif_class_members:
                raise KeyError(f"'{name}' does not belong to {GIFCreator} members.")
            correct_type = type(getattr(self, name))

            # type check
            assert isinstance(value, correct_type), \
                TypeError(f'{name} type need {correct_type.__name__} not {type(value).__name__}')

            setattr(self, '_GIFCreator__' + name.lower(), value)

    def record(self, draw_func: Callable = None, **options):
        """

        :param draw_func:
        :param options:
                - fps
                - start_after: milliseconds. While waiting, white pictures will continuously
                generate to used as the heading image of GIF.
                - end_after:
        :return:
        """
        if draw_func and callable(draw_func):
            setattr(self, 'draw', draw_func)
        if not (hasattr(self, 'draw') and callable(getattr(self, 'draw'))):
            raise NotImplementedError('subclasses of GIFCreatorMixin must provide a draw() method')

        regex = re.compile(fr"""{self.name}_[0-9]{{5}}""")

        def wrap():
            self.draw()
            turtle.ontimer(self._stop, options.get('end_after', 0))

        wrap_draw = functools.wraps(self.draw)(wrap)

        try:
            # https://blog.csdn.net/lingyu_me/article/details/105400510
            # Does a turtle.clear() and then resets this turtle's state (i.e. direction, position etc.)
            turtle.reset()
        except turtle.Terminator:
            turtle.reset()

        if self.REBUILD:
            for f in [_ for _ in self.temp_dir.glob(f'*.*') if _.suffix.upper().endswith(('EPS', 'PNG'))]:
                [os.remove(f) for ls in regex.findall(str(f)) if ls is not None]

        self._start()
        self._save()  # init start the recording
        turtle.ontimer(wrap_draw,
                       t=options.get('start_after', 0))  # start immediately
        turtle.done()
        print('convert_eps2image...')
        self.convert_eps2image()
        print('make_gif...')
        self.make_gif(fps=options.get('fps'))
        print(f'done:{self.name}')
        self._cleanup()
        return

    def convert_eps2image(self):
        """
        image extension (PGM, PPM, GIF, PNG) is all compatible with tk.PhotoImage
        .. important:: you need to use ghostscript, see ``init()``
        """
        for eps_file in [_ for _ in self.temp_dir.glob('*.*') if _.suffix.upper() == '.EPS']:
            output_path = self.temp_dir / Path(eps_file.name + '.png')
            if output_path.exists():
                continue
            with PIL.Image.open(str(eps_file)) as im:
                im.save(output_path, 'png')

    @staticmethod
    def natural_sort(a_list: list):
        convert = lambda text: int(text) if text.isdigit() else text.lower()
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', os.path.basename(key))]
        return a_list.sort(key=alphanum_key)

    def make_gif(self, output_name=None, **options):
        """
        :param output_name: basename `xxx.png` or `xxx`
        :param options:
            - fps: for GIF
        :return:
        """

        if output_name is None:
            output_name = self.__name

        if not output_name.lower().endswith('.gif'):
            output_name += '.gif'

        image_list = [_ for _ in self.temp_dir.glob(f'*.*') if
                      (_.suffix.upper().endswith(('PGM', 'PPM', 'GIF', 'PNG')))
                      ]
        if not image_list:
            sys.stderr.write(f'No image found in {self.temp_dir}')
            return
        self.natural_sort(image_list)

        output_path = Path(self.BASE_PATH) / Path(f'{output_name}')
        fps = options.get('fps', options.get('FPS'))
        if fps is None:
            fps = 1000 / self.duration
        make_gif(image_list, output_path, fps=fps, loop=0)
        # open the output folder
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, self.BASE_PATH])

    def _start(self):
        self.__is_running = True

    def _stop(self):
        print(f'finished draw:{self.name}')
        self.__is_running = False
        self.__counter = 1

    def _save(self):
        if self.__is_running:
            # print(self.__counter)
            output_file: Path = self.temp_dir / Path(f'{self.__counter:05d}.eps')
            if not output_file.exists():
                # 0001.eps, 0002.eps ...
                turtle.getcanvas().postscript(file=output_file)
            self.__counter += 1
            # trigger only once, so we need to set it again.
            turtle.ontimer(self._save, t=self.duration)

    def _cleanup(self):
        shutil.rmtree(self.temp_dir)