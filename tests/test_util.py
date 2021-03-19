# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from src.util.io import check_axiom_syntax, check_rule_syntax, validate_args


class TestUtil(unittest.TestCase):

    def test_check_axiom_syntax(self):
        correct_axioms = ["F", "ff", "+++", "----", "fF", "F+F", "F+F-f-F"]
        for axiom in correct_axioms:
            self.assertTrue(check_axiom_syntax(axiom))
        incorrect_axioms = ["G", "lf", "++|", "-$--", "fF|", "F=F", "F#F@f*F"]
        for axiom in incorrect_axioms:
            self.assertFalse(check_axiom_syntax(axiom))

    def test_check_rule_syntax(self):
        correct_rules = ["F", "ff", "+++", "----", "fF", "F+F", "F+F-f-F"]
        for rule in correct_rules:
            self.assertTrue(check_rule_syntax(rule))
        incorrect_rules = ["G=F", "l=f", "++F", "A=-$--", "f=fF|", "F=F=", "F#F@f*F"]
        for rule in incorrect_rules:
            self.assertFalse(check_rule_syntax(rule))

    def test_validate_args(self):
        axioms = ["F", "F+f", "F+F-f-f"]
        production = ["F=F+F", "F=f-F+f", "F=FF-ff"]
        iterations = [2, 3, 90]
        delta = [0, 90, 180]
        for idx in 0..length(axioms):
            try:
                validate_args(axioms[idx], production[idx], iterations[idx], delta[idx])
            except:
                self.fail("Expected valid arguments")

        axioms = ["G", "F+f", "F+F-f-f", "FFFFF"]
        production = ["F=F+F", "Ff-F+f", "F=FF-ff", "F=FFF-ff++f"]
        iterations = [2, 3, -9, 90]
        delta = [0, 90, 180, 270]
        for idx in 0..len(axioms):
            try:
                validate_args(axioms[idx], production[idx], iterations[idx], delta[idx])
                self.fail("Expected invalid arguments")
            except:
                continue


if __name__ == '__main__':
    unittest.main()
