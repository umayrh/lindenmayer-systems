
def _develop_sequence(axiom: str, productions: dict[str, str], iterations: int) -> str:
    if iterations <= 0:
        return axiom
    corollary = ""
    for letter in axiom:
        # the default production is identity
        corollary += productions[letter] if letter in productions else letter
    return _develop_sequence(corollary, productions, iterations - 1)

def _make_rule_map(productions: list[str]) -> dict[str, str]:
    productions_map: dict[str, str] = {}
    for production in productions:
        rules_sides = production.split("=")
        productions_map[rules_sides[0]] = rules_sides[1]
    return productions_map

def develop_sequence(axiom: str, productions: list[str], iterations: int) -> str:
    return _develop_sequence(axiom, _make_rule_map(productions), iterations)
