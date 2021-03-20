# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from src.compose.sequence import develop_sequence


class TestSequence(unittest.TestCase):

    def test_develop_sequence(self):
        axioms = ["F", "F+f", "F+F-f-f"]
        production = [["F=F+F"], ["F=f-F"], ["F=FF-ff", "f=f+F"]]
        iterations = [3, 2, 1]
        expected = ["F+F+F+F+F+F+F+F", "f-f-F+f", "FF-ff+FF-ff-f+F-f+F"]
        for idx in range(len(axioms)):
            try:
                self.assertEqual(expected[idx],
                                 develop_sequence(axioms[idx], production[idx], iterations[idx]))
            except:
                self.fail("Expected valid arguments")


if __name__ == '__main__':
    unittest.main()
