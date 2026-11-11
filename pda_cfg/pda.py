from collections import deque
import re

def balanced_parentheses_pda(text):
    stack = []
    trace = []
    for position, symbol in enumerate(text, start=1):
        if symbol == "(":
            stack.append("(")
            action = "PUSH ("
        elif symbol == ")":
            if not stack:
                trace.append((position, symbol, "".join(stack) or "EMPTY", "REJECT: no opening bracket"))
                return False, trace
            stack.pop()
            action = "POP ("
        else:
            trace.append((position, symbol, "".join(stack) or "EMPTY", "REJECT: invalid symbol"))
            return False, trace
        trace.append((position, symbol, "".join(stack) or "EMPTY", action))
    return len(stack) == 0, trace

def palindrome_marker_pda(text):
    if text.count("#") != 1:
        return False, [], "Input must contain exactly one # separator."
    left, right = text.split("#")
    if any(ch not in "ab" for ch in left + right):
        return False, [], "Only a, b and # are allowed."
    stack = []
    trace = []
    for i, ch in enumerate(left, start=1):
        stack.append(ch)
        trace.append((i, ch, "".join(stack), f"PUSH {ch}"))
    trace.append((len(left) + 1, "#", "".join(stack) or "EMPTY", "Middle marker: switch to matching"))
    offset = len(left) + 2
    for j, ch in enumerate(right, start=offset):
        if not stack or stack[-1] != ch:
            trace.append((j, ch, "".join(stack) or "EMPTY", "REJECT: mismatch"))
            return False, trace, "The right half does not match the reverse of the left half."
        stack.pop()
        trace.append((j, ch, "".join(stack) or "EMPTY", f"MATCH and POP {ch}"))
    accepted = not stack
    return accepted, trace, "All symbols matched." if accepted else "REJECT: unmatched symbols remain."

# CFG-to-PDA style parser. Stack top is the rightmost item.
def tokenize_expression(source):
    tokens = []
    i = 0
    while i < len(source):
        if source[i].isspace():
            i += 1
        elif source[i].isalpha() or source[i].isdigit():
            j = i + 1
            while j < len(source) and (source[j].isalnum() or source[j] == "_"):
                j += 1
            tokens.append("id")
            i = j
        elif source[i] in "+*()":
            tokens.append(source[i])
            i += 1
        else:
            raise ValueError(f"Invalid character: {source[i]}")
    return tokens

PRODUCTIONS = {
    "E": [["T", "E1"]],
    "E1": [["+", "T", "E1"], []],
    "T": [["F", "T1"]],
    "T1": [["*", "F", "T1"], []],
    "F": [["(", "E", ")"], ["id"]],
}
NONTERMINALS = set(PRODUCTIONS)

def arithmetic_cfg_pda(source, max_steps=10000):
    try:
        tokens = tokenize_expression(source)
    except ValueError as error:
        return False, [], str(error)
    # Configuration: (remaining input index, stack tuple); bottom marker is $
    queue = deque([(0, ("$", "E"))])
    visited = set()
    trace = []
    steps = 0
    while queue and steps < max_steps:
        index, stack = queue.popleft()
        steps += 1
        if (index, stack) in visited:
            continue
        visited.add((index, stack))
        if not stack:
            continue
        top = stack[-1]
        rest = stack[:-1]
        if top == "$":
            if index == len(tokens):
                trace.append((index, "$", "ACCEPT", "Input consumed and stack finished"))
                return True, trace, "Expression accepted."
            continue
        if top in NONTERMINALS:
            for production in PRODUCTIONS[top]:
                new_stack = rest + tuple(reversed(production))
                label = "ε" if not production else " ".join(production)
                trace.append((index, top, " ".join(new_stack), f"EXPAND {top} -> {label}"))
                queue.append((index, new_stack))
        elif index < len(tokens) and top == tokens[index]:
            new_stack = rest
            trace.append((index + 1, tokens[index], " ".join(new_stack) or "EMPTY", f"MATCH {top}"))
            queue.append((index + 1, new_stack))
    return False, trace[-30:], "Expression rejected (syntax does not match the grammar)."
