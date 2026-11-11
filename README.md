# FLA Task 3 – CFG and PDA Case Studies

**Student:** Ronav Js Gop  
**Register Number:** RA2411026050071  
**Course:** 21CSC301T – Formal Language and Automata  
**Assignment:** Case Study-Based Analysis and Design using PDA and CFG

A beginner-friendly Python project demonstrating three case studies:
1. Balanced parentheses
2. Arithmetic expression validation
3. Palindrome checking with a middle marker `#`

## Requirements
- Python 3.9 or newer
- No external packages are required

## Run the project
Open a terminal in this folder and run:

```bash
python main.py
```

Run one case study:

```bash
python main.py brackets
python main.py expression
python main.py palindrome
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## What each folder contains

- `main.py` – starts the project
- `pda_cfg/grammar.py` – CFG production rules and sample derivations
- `pda_cfg/pda.py` – stack-based PDA simulations and expression parser
- `pda_cfg/cases.py` – sample accepted/rejected strings and demonstrations
- `tests/` – automatic tests
- `docs/diagrams/` – Mermaid state diagrams

## Case Study 1: Balanced parentheses

CFG:
```text
S → (S)S | ε
```

The PDA pushes an opening parenthesis onto the stack. When it reads a closing parenthesis, it pops one opening parenthesis. It rejects if a closing parenthesis has nothing to match. It accepts if the input ends with an empty stack.

## Case Study 2: Arithmetic expressions

Tokens: `id`, `+`, `*`, `(`, `)`.

CFG (with multiplication precedence):
```text
E  → T E1
E1 → + T E1 | ε
T  → F T1
T1 → * F T1 | ε
F  → ( E ) | id
```

The program uses a CFG-driven stack parser. The grammar separates expression, term and factor, so multiplication has higher precedence than addition. The parser's production choices are explored as stack transitions.

## Case Study 3: Palindrome with a separator

Language: `w#wᴿ`, where `w` is any string of `a` and `b`, and `wᴿ` is its reverse.

CFG:
```text
S → aSa | bSb | #
```

The PDA pushes the symbols before `#`. After `#`, it compares each input symbol with the top of the stack and pops matching symbols.

## Important note

A PDA is a theoretical machine with a stack. The arithmetic-expression case uses a PDA-style CFG parsing stack: it expands grammar variables and matches terminals. This is a nondeterministic CFG-to-PDA simulation, while the chosen grammar itself is unambiguous.
