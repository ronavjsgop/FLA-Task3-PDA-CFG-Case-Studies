BRACKETS_CFG = [
    ("S", ["(", "S", ")", "S"]),
    ("S", []),  # epsilon
]

ARITHMETIC_CFG = {
    "E": [["T", "E1"]],
    "E1": [["+", "T", "E1"], []],
    "T": [["F", "T1"]],
    "T1": [["*", "F", "T1"], []],
    "F": [["(", "E", ")"], ["id"]],
}

PALINDROME_CFG = [
    ("S", ["a", "S", "a"]),
    ("S", ["b", "S", "b"]),
    ("S", ["#"]),
]

def show_grammar(title, productions):
    print(f"\n{title}")
    for left, right in productions:
        print(f"  {left} -> {' '.join(right) if right else 'ε'}")

def bracket_derivation():
    # S => (S)S => ((S)S)S => (()) 
    return ["S", "(S)S", "((S)S)S", "(()S)S", "(())S", "(())"]

def palindrome_derivation():
    return ["S", "aSa", "abSba", "ab#ba"]
