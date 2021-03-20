from src.util.io import get_args, validate_args
from src.compose.sequence import develop_sequence
from src.plotter.plot import make_plot
from src.plotter.write_gif import GIFCreator

def plot_turtle():
    #axiom, productions, iterations, delta = get_args()
    #validate_args(axiom, productions, iterations, delta)
    axiom = "F-F-F-F"
    productions = ["F=F-F+F+FF-F-F+F"]
    iterations = 3
    delta = 90
    initial_x = -200
    initial_y = 40
    step_size = 4
    sequence_result = develop_sequence(axiom, productions, iterations)

    class LsystemGif(GIFCreator):
        DURATION = 200  # optional
        def draw(self):
            make_plot(sequence_result, delta, step_size, initial_x, initial_y, drawing_speed=10)
    LsystemGif(name='Quadratic Koch island').record(
        fps=1
        # fps=, start_after=, end_after=  <-- optional
    )

if __name__ == '__main__':
    plot_turtle()

