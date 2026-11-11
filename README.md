# FLA Task 3 – Case Study-Based Analysis and Design Using PDA and CFG

## Project Information

**Institution:** SRM Institute of Science and Technology, Tiruchirappalli  
**Course:** 21CSC301T – Formal Language and Automata  
**Department:** Artificial Intelligence and Machine Learning  
**Semester:** V  
**Academic Year:** 2026–2027  
**Assessment:** Continuous Learning Assessment – 2 (Task 3)

**Submitted By:** Ronav Js Gop  
**Register Number:** RA2411026050071

---

## 1. Project Overview

This project focuses on the analysis and implementation of Context-Free Grammars (CFG) and Pushdown Automata (PDA) through practical case studies using Python.

The main objective is to understand how formal language theory can be applied to validate different types of input strings using grammar production rules and stack-based automata.

The project demonstrates three important applications:

1. Balanced Parentheses Validation
2. Arithmetic Expression Validation
3. Palindrome Checking Using a Middle Separator

Each case study includes a definition of the target language, CFG production rules, PDA processing logic, sample derivations, and accepted and rejected test cases.

The implementation uses Python to simulate the behaviour of Pushdown Automata and CFG-based parsing.

## 2. Objectives

- Understand the concepts of Context-Free Grammars and Pushdown Automata.
- Design CFG production rules for different languages.
- Implement stack-based PDA simulations using Python.
- Validate strings based on their grammatical structure.
- Demonstrate successful and unsuccessful processing examples.
- Understand the importance of stack memory in recognizing context-free languages.
- Explore grammar-based parsing and expression validation.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Implementation of CFG and PDA simulations |
| Stack | Store and process symbols |
| Context-Free Grammar | Define valid language structures |
| Pushdown Automata | Validate input strings |
| Unit Testing | Verify accepted and rejected inputs |
| Git and GitHub | Version control and project hosting |

No external Python packages are required.

## 4. Case Studies

### Case Study 1: Balanced Parentheses Validation

**Problem Description:**

Balanced parentheses validation checks whether every opening parenthesis has a corresponding closing parenthesis in the correct order.

**Target Language:**

L = { w ∈ {(, )}* | w contains properly balanced parentheses }

**CFG Production Rules:**

```text
S → (S)S | ε
```

Where:
- S represents the starting non-terminal.
- ε represents the empty string.
- `(S)S` represents a balanced group followed by another balanced sequence.

**PDA Working Principle:**

1. Read the input string from left to right.
2. Push an opening parenthesis `(` onto the stack.
3. When a closing parenthesis `)` is encountered, pop one opening parenthesis.
4. If a closing parenthesis appears when the stack is empty, reject the string.
5. Accept if the entire input is processed and the stack is empty.

**Accepted Examples:**

```text
()
(())
()()
```

**Rejected Examples:**

```text
(()
())
)(
```

**Real-World Applications:**
- Syntax checking in programming languages.
- Compiler design.
- Validation of mathematical expressions.
- Checking nested structures in source code.

### Case Study 2: Arithmetic Expression Validation

**Problem Description:**

Arithmetic expression validation checks whether a mathematical expression follows the correct grammatical structure.

The project supports identifiers, numbers, addition, multiplication, and parentheses.

**Target Language:**

Valid arithmetic expressions formed using operands, the operators `+` and `*`, and properly matched parentheses.

**CFG Production Rules:**

```text
E  → T E1
E1 → + T E1 | ε
T  → F T1
T1 → * F T1 | ε
F  → (E) | id
```

Where:
- E represents an expression.
- T represents a term.
- F represents a factor.
- id represents an identifier or number.
- E1 and T1 represent the remaining expression and term components.

**PDA Working Principle:**

1. Tokenize the input expression.
2. Initialize the parsing stack with the starting grammar symbol.
3. Expand non-terminal symbols using CFG production rules.
4. Match terminal symbols with the input tokens.
5. Explore possible grammar expansions using stack transitions.
6. Accept if all input tokens are consumed and the stack is completed.

The grammar gives multiplication higher precedence than addition.

**Accepted Examples:**

```text
a+b
a*b
a+b*c
(a+b)*c
12 + total2
```

**Rejected Examples:**

```text
a++b
a+*b
(a+b
+a
a/ b
```

**Real-World Applications:**
- Compiler construction.
- Programming language syntax validation.
- Mathematical expression parsing.
- Syntax analysis in interpreters.

### Case Study 3: Palindrome Checking Using a Middle Separator

**Problem Description:**

A palindrome is a string that reads the same forward and backward.

This case study checks palindromes using `#` as a middle separator between the original string and its reverse.

**Target Language:**

L = { w#wᴿ | w ∈ {a,b}* }

Here, wᴿ represents the reverse of w.

**CFG Production Rules:**

```text
S → aSa
S → bSb
S → #
```

**PDA Working Principle:**

1. Read the symbols before the separator `#`.
2. Push each symbol onto the stack.
3. When `#` is encountered, switch to the matching phase.
4. Read the remaining symbols one by one.
5. Compare each symbol with the top of the stack.
6. Pop the stack when the symbols match.
7. Accept if all symbols match and the stack becomes empty.

**Accepted Examples:**

```text
#
a#a
b#b
ab#ba
aa#aa
```

**Rejected Examples:**

```text
ab#ab
aa#bb
a#b
ab#b
ab##ba
```

**Real-World Applications:**
- String pattern recognition.
- Formal language processing.
- Symmetry checking.
- Theoretical models of language recognition.

## 5. Why Pushdown Automata Are Required

Finite Automata have limited memory and cannot maintain an unlimited count of opening parentheses or remember an arbitrary sequence of symbols for later comparison.

Pushdown Automata overcome this limitation by using a stack.

In this project:
- Balanced parentheses require stack-based matching.
- Arithmetic expression validation requires grammar-based parsing.
- Palindrome checking requires storing and comparing symbols using a stack.

Therefore, PDA and CFG provide suitable computational models for these context-free language problems.

## 6. Project Structure

```text
FLA-Task3-PDA-CFG-Case-Studies/
│
├── main.py
│
├── pda_cfg/
│   ├── __init__.py
│   ├── cases.py
│   ├── grammar.py
│   └── pda.py
│
├── tests/
│   └── test_cases.py
│
├── docs/
│   └── diagrams/
│       ├── arithmetic_expression.md
│       ├── balanced_parentheses.md
│       └── palindrome.md
│
├── .gitignore
└── README.md
```

### File Descriptions

- **main.py:** Main entry point used to execute the case studies.
- **cases.py:** Contains demonstrations and sample accepted and rejected inputs.
- **grammar.py:** Defines CFG production rules and sample derivations.
- **pda.py:** Implements stack-based PDA simulations and the arithmetic CFG parser.
- **test_cases.py:** Contains automated unit tests for all three case studies.
- **docs/diagrams/:** Contains state diagrams for the three case studies.
- **.gitignore:** Specifies files and folders excluded from Git tracking.

## 7. Installation and Execution

**Prerequisites:**
- Python 3.6 or newer.
- Git (optional, for repository management).
- Visual Studio Code or any Python-supported editor.

**Step 1: Clone the Repository**

```bash
git clone https://github.com/ronavjsgop/FLA-Task3-PDA-CFG-Case-Studies.git
```

**Step 2: Navigate to the Project Folder**

```bash
cd FLA-Task3-PDA-CFG-Case-Studies
```

**Step 3: Run All Case Studies**

```bash
python main.py
```

**Step 4: Run Individual Case Studies**

Balanced Parentheses:

```bash
python main.py brackets
```

Arithmetic Expression:

```bash
python main.py expression
```

Palindrome Checking:

```bash
python main.py palindrome
```

**Step 5: Execute Unit Tests**

```bash
python -m unittest discover -s tests -v
```

## 8. Testing and Validation

The project uses Python's built-in unittest framework to verify the correctness of the three case studies.

The test cases cover:
- Valid and invalid balanced parentheses.
- Correct and incorrect arithmetic expressions.
- Matching and non-matching palindrome strings.

Both accepted and rejected inputs are tested to ensure that the implemented models behave as expected.

## 9. Ambiguity and Determinism

A Context-Free Grammar may sometimes generate multiple parse trees for the same input, resulting in ambiguity.

The arithmetic grammar used in this project separates expressions, terms, and factors to establish operator precedence. This makes the selected grammar unambiguous for the supported operators.

The arithmetic parser explores possible grammar expansions using a queue of stack configurations. The balanced-parentheses and palindrome implementations use deterministic stack-processing procedures for their respective input formats.

## 10. Expected Learning Outcomes

After completing this project, the following concepts are understood:

- Design and implementation of Context-Free Grammars.
- Working principles of Pushdown Automata.
- Stack operations such as PUSH and POP.
- Grammar-based arithmetic expression parsing.
- Validation of context-free language patterns.
- Differences between Finite Automata and Pushdown Automata.
- Testing and verification of formal language models.

## 11. Conclusion

This project demonstrates the practical application of Context-Free Grammars and Pushdown Automata through three different case studies.

Balanced parentheses validation demonstrates stack-based symbol matching, arithmetic expression validation demonstrates grammar-driven parsing and operator precedence, and palindrome checking demonstrates symbol storage and reverse comparison using a stack.

The Python implementation provides a simple and practical understanding of formal language concepts. It also highlights the importance of CFG and PDA in compiler design, syntax validation, and language processing.

---

**Submitted by:** Ronav Js Gop  
**Register Number:** RA2411026050071  
**Course:** Formal Language and Automata (21CSC301T)
