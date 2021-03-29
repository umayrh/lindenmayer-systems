import unittest

from src.plotter.main import _make_gif, PlotProperties

class TestAbop14(unittest.TestCase):
    # ABOP Fig 1.10a
    def test_make_gif_koch_1_10a(self):
        axiom = "L"
        productions = ["L=L+R+", "R=-L-R"]
        iterations = 10
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=100, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.10a - dragon curve"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.10b
    def test_make_gif_koch_1_10b(self):
        axiom = "R"
        productions = ["L=R+L+R", "R=L-R-L"]
        iterations = 6
        delta = 60
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=100, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.10b - Sierpinski gasket"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.11a
    def test_make_gif_koch_1_11a(self):
        axiom = "L"
        productions = ["L=L+R++R-L--LL-R+", "R=-L+RR++R+L--L-R"]
        iterations = 4
        delta = 60
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=100, step_size=5, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.11a - hexagonal Gosper curve"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.11b
    def test_make_gif_koch_1_11b(self):
        axiom = "-R"
        productions = ["L=LL-R-R+L+L-R-RL+R+LLR-L+R+LL+R-LR-R-L+L+RR-",
                       "R=+LL-R-R+L+LR+L-RR-L-R+LRR-L-RL+L+R-R-L+L+RR"]
        iterations = 2
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=100, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.11b - quadratic Gosper curve"
        _make_gif(axiom, productions, iterations, delta, properties)

if __name__ == '__main__':
    unittest.main()
