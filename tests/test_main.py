# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from src.plotter.main import _make_gif, PlotProperties

"""
Quadratic Koch island:
    axiom = "F-F-F-F"
    productions = ["F=F-F+F+FF-F-F+F"]
Quadratic snowflake:
    axiom = "-F"
    productions = ["F=F+F-F-F+F"]

"""
class TestMain(unittest.TestCase):
    # ABOP Fig 1.6
    def test_make_gif_quad_koch_island(self):
        axiom = "F-F-F-F"
        productions = ["F=F-F+F+FF-F-F+F"]
        iterations = 3
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=40, step_size=4, base_path="../data")
        properties.name = "Quadratic Koch island"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.7a
    def test_make_gif_quad_koch_island_2(self):
        axiom = "F-F-F-F"
        productions = ["F=F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F"]
        iterations = 2
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=40, step_size=4, base_path="../data")
        properties.name = "Quadratic Koch island - 2"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.7b
    def test_make_gif_quad_snow_flake(self):
        axiom = "-F"
        productions = ["F=F+F-F-F+F"]
        iterations = 4
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=400, step_size=8, fps=1, base_path="../data")
        properties.name = "Quadratic snowflake"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.7c
    def test_make_gif_island_and_lakes(self):
        axiom = "F+F+F+F"
        productions = ["F=F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF", "f=ffffff"]
        iterations = 2
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=-200, step_size=8, fps=1, base_path="../data")
        properties.name = "Islands and Lakes"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.8a
    def test_make_gif_koch_1_8a(self):
        axiom = "F-F-F-F"
        productions = ["F=FF-F-F-F-F-F+F"]
        iterations = 4
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=0, initial_y=300, step_size=8, fps=1, drawing_speed=0, base_path="../data")
        properties.name = "1.8a - a Koch curve"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.8b
    def test_make_gif_koch_1_8b(self):
        axiom = "F-F-F-F"
        productions = ["F=FF-F-F-F-FF"]
        iterations = 4
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=300, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.8b - a Koch curve"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.8c
    def test_make_gif_koch_1_8c(self):
        axiom = "F-F-F-F"
        productions = ["F=FF-F+F-F-FF"]
        iterations = 4
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=300, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.8c - a Koch curve"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.8d
    def test_make_gif_koch_1_8d(self):
        axiom = "F-F-F-F"
        productions = ["F=FF-F--F-F"]
        iterations = 4
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=300, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.8d - a Koch curve"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.8e
    def test_make_gif_koch_1_8e(self):
        axiom = "F-F-F-F"
        productions = ["F=F-FF--F-F"]
        iterations = 5
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-0, initial_y=0, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.8e - a Koch curve"
        _make_gif(axiom, productions, iterations, delta, properties)

    # ABOP Fig 1.8f
    def test_make_gif_koch_1_8f(self):
        axiom = "F-F-F-F"
        productions = ["F=F-F+F-F-F"]
        iterations = 5
        delta = 90
        properties: PlotProperties = PlotProperties(
            initial_x=-200, initial_y=100, step_size=4, fps=0.5, drawing_speed=0, base_path="../data")
        properties.name = "1.8f - a Koch curve"
        _make_gif(axiom, productions, iterations, delta, properties)

if __name__ == '__main__':
    unittest.main()
