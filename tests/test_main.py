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

    def test_make_gif_quad_koch_island(self):
        axiom = "F-F-F-F"
        productions = ["F=F-F+F+FF-F-F+F"]
        iterations = 3
        delta = 90
        initial_x = -200
        initial_y = 40
        step_size = 4
        properties: PlotProperties = PlotProperties(
            initial_x=initial_x, initial_y=initial_y,step_size=step_size)
        properties.name = "Quadratic Koch island"
        _make_gif(axiom, productions, iterations, delta, properties)

    def test_make_gif_quad_snow_flake(self):
        axiom = "-F"
        productions = ["F=F+F-F-F+F"]
        iterations = 3
        delta = 90
        properties: PlotProperties = PlotProperties()
        properties.name = "Quadratic snowflake"
        _make_gif(axiom, productions, iterations, delta, properties)

if __name__ == '__main__':
    unittest.main()
