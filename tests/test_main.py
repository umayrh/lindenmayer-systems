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

if __name__ == '__main__':
    unittest.main()
