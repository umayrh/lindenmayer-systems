import re
import argparse

def get_args() -> tuple:
    parser = argparse.ArgumentParser(description='Process input axioms and productions.')
    parser.add_argument('-a', '--axiom', help='An axiom in turtle interpretation', type=str)
    parser.add_argument('-p', '--productions', help='A comma-separated list of production rules',
                        type=lambda s: [str(production) for production in s.split(',')])
    parser.add_argument('-n', '--iterations', help='The length of the development sequence', type=int)
    parser.add_argument('-d', '--delta', help='The angle, in degrees, of the heading', type=int)
    args = parser.parse_args()
    return args.axiom, args.productions, args.iterations, args.delta

def check_axiom_syntax(turtle_str: str) -> bool:
    if not turtle_str:
        return False
    reg = re.compile('^[fF+-]+$')
    return bool(reg.match(turtle_str))

def check_rule_syntax(turtle_str: str) -> bool:
    if not turtle_str or len(turtle_str) < 3:
        return False
    reg = re.compile('^[fF+-=]+$')
    print(f'working on: {turtle_str}')
    return bool(reg.match(turtle_str)) and turtle_str[1] == "=" and turtle_str.count("=") == 1

def validate_args(axiom: str, productions: list[str], iterations: int, delta: int):
    assert check_axiom_syntax(axiom), "Bad syntax for axiom"
    assert all([check_rule_syntax(production) for production in productions]), "Bad syntax for production rule(s)"
    # TODO need a check for DOL constraint e.g. LHS of each rules must be unique across rules
    assert iterations >= 1, "Number of iteration must be a positive integer"
    assert 0 <= delta <= 180, "Angle must be between 0 and 180 (inclusive)"
