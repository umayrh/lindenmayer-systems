import unittest

from src.plotter.main import _make_gif, PlotProperties

class TestAbop13(unittest.TestCase):
    # ABOP Fig 1.6
    def test_make_gif_quad_koch_island(self):
        axiom = "F-F-F-F"
        productions = ["F=F-F+F+FF-F-F+F"]
        iterations = 3
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=40, step_size=4, base_path="../data")
        properties.name = "1.6 - Quadratic Koch island"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.7a
    def test_make_gif_quad_koch_island_2(self):
        axiom = "F-F-F-F"
        productions = ["F=F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F"]
        iterations = 2
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=40, step_size=4, base_path="../data")
        properties.name = "1.7a Quadratic Koch island"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.7b
    def test_make_gif_quad_snow_flake(self):
        axiom = "-F"
        productions = ["F=F+F-F-F+F"]
        iterations = 4
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=400, step_size=8, fps=1, base_path="../data")
        properties.name = "1.7b - Quadratic snowflake"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.8
    def test_make_gif_island_and_lakes(self):
        axiom = "F+F+F+F"
        productions = ["F=F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF", "f=ffffff"]
        iterations = 2
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=-200, step_size=8, fps=1, base_path="../data")
        properties.name = "1.8 - Islands and Lakes"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.9a
    def test_make_gif_koch_1_9a(self):
        axiom = "F-F-F-F"
        productions = ["F=FF-F-F-F-F-F+F"]
        iterations = 4
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=0, initial_y=300, step_size=8, fps=1, drawing_speed=0, base_path="../data")
        properties.name = "1.9a - a Koch curve"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.9b
    def test_make_gif_koch_1_9b(self):
        axiom = "F-F-F-F"
        productions = ["F=FF-F-F-F-FF"]
        iterations = 4
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=300, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.9b - a Koch curve"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.8c
    def test_make_gif_koch_1_9c(self):
        axiom = "F-F-F-F"
        productions = ["F=FF-F+F-F-FF"]
        iterations = 4
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=300, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.9c - a Koch curve"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.9d
    def test_make_gif_koch_1_9d(self):
        axiom = "F-F-F-F"
        productions = ["F=FF-F--F-F"]
        iterations = 4
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=300, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.9d - a Koch curve"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.9e
    def test_make_gif_koch_1_9e(self):
        axiom = "F-F-F-F"
        productions = ["F=F-FF--F-F"]
        iterations = 5
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-0, initial_y=0, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.9e - a Koch curve"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.9f
    def test_make_gif_koch_1_9f(self):
        axiom = "F-F-F-F"
        productions = ["F=F-F+F-F-F"]
        iterations = 5
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=100, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.9f - a Koch curve"
        _make_gif(axiom, productions, iterations, delta, properties)

if __name__ == '__main__':
    unittest.main()
