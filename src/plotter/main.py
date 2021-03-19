from src.util.io import get_args, validate_args
from src.compose.sequence import develop_sequence

def plot_turtle():
    axiom, productions, iterations, delta = get_args()
    validate_args(axiom, productions, iterations, delta)
    sequence_result = develop_sequence(axiom, productions, iterations)

