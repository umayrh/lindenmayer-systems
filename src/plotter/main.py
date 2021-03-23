from src.util.io import get_args, validate_args
from src.compose.sequence import develop_sequence
from src.plotter.plot import make_plot
from src.plotter.write_gif import GIFCreator

class PlotProperties:
    def __init__(self,
                 initial_x: int = -200,
                 initial_y: int = 40,
                 step_size: int = 4,
                 drawing_speed: int = 10,
                 fps: int = 5,
                 name: str = "L-system Plot"):
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.step_size = step_size
        self.drawing_speed = drawing_speed
        self.fps = fps
        self.name = name

def _make_gif(_axiom: str,
              _productions: list[str],
              _iterations: int,
              _delta: int,
              _properties: PlotProperties):
    sequence_result = develop_sequence(_axiom, _productions, _iterations)

    duration = int(1000 / _properties.fps)
    class LsystemGif(GIFCreator):
        DURATION = duration
        def draw(self):
            make_plot(sequence_result,
                      _delta,
                      _properties.step_size,
                      _properties.initial_x,
                      _properties.initial_y,
                      _properties.drawing_speed)
    LsystemGif(name=_properties.name,duration=duration).record(
        # fps=, start_after=, end_after=  <-- optional
        fps=_properties.fps
    )

def plot_turtle():
    _axiom, _productions, _iterations, _delta = get_args()
    validate_args(_axiom, _productions, _iterations, _delta)
    _make_gif(_axiom, _productions, _iterations, _delta)

if __name__ == '__main__':
    plot_turtle()
