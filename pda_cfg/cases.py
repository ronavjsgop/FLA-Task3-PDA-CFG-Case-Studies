from .grammar import show_grammar, BRACKETS_CFG, ARITHMETIC_CFG, PALINDROME_CFG, bracket_derivation, palindrome_derivation
from .pda import balanced_parentheses_pda, arithmetic_cfg_pda, palindrome_marker_pda

def print_trace(trace):
    print("Step | Read | Stack / Next stack | Action")
    print("-" * 72)
    for i, row in enumerate(trace, start=1):
        print(f"{i:>4} | {str(row[1]):>4} | {str(row[2]):<24} | {row[3]}")

def run_brackets():
    print("\n=== CASE STUDY 1: BALANCED PARENTHESES ===")
    show_grammar("CFG:", BRACKETS_CFG)
    print("Derivation for (()) : " + " => ".join(bracket_derivation()))
    for sample in ["()", "(())", "()()", "(()", "())", ")("]:
        accepted, trace = balanced_parentheses_pda(sample)
        print(f"\nInput: {sample!r} -> {'ACCEPTED' if accepted else 'REJECTED'}")
        print_trace(trace)

def run_expression():
    print("\n=== CASE STUDY 2: ARITHMETIC EXPRESSION ===")
    show_grammar("CFG:", [(left, right) for left, options in ARITHMETIC_CFG.items() for right in options])
    for sample in ["a+b", "a+b*c", "(a+b)*c", "a++b", "a+*b", "(a+b"]:
        accepted, trace, message = arithmetic_cfg_pda(sample)
        print(f"\nInput: {sample!r} -> {'ACCEPTED' if accepted else 'REJECTED'} ({message})")
        print_trace(trace)

def run_palindrome():
    print("\n=== CASE STUDY 3: PALINDROME WITH # MIDDLE MARKER ===")
    show_grammar("CFG:", PALINDROME_CFG)
    print("Derivation for ab#ba : " + " => ".join(palindrome_derivation()))
    for sample in ["ab#ba", "aa#aa", "a#a", "ab#ab", "aa#bb", "a#b"]:
        accepted, trace, message = palindrome_marker_pda(sample)
        print(f"\nInput: {sample!r} -> {'ACCEPTED' if accepted else 'REJECTED'} ({message})")
        print_trace(trace)

def run_all():
    run_brackets()
    run_expression()
    run_palindrome()
