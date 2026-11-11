import unittest
from pda_cfg.pda import balanced_parentheses_pda, arithmetic_cfg_pda, palindrome_marker_pda

class TestCaseStudies(unittest.TestCase):
    def test_balanced_parentheses(self):
        for value in ["", "()", "(())", "()()"]:
            self.assertTrue(balanced_parentheses_pda(value)[0], value)
        for value in ["(()", "())", ")(", "(a)"]:
            self.assertFalse(balanced_parentheses_pda(value)[0], value)

    def test_arithmetic_expressions(self):
        for value in ["a+b", "a*b", "a+b*c", "(a+b)*c", "12 + total2"]:
            self.assertTrue(arithmetic_cfg_pda(value)[0], value)
        for value in ["a++b", "a+*b", "(a+b", "a b", "+a", "a/ b"]:
            self.assertFalse(arithmetic_cfg_pda(value)[0], value)

    def test_palindromes_with_separator(self):
        for value in ["#","a#a","b#b","ab#ba","aa#aa","aba#aba"]:
            self.assertTrue(palindrome_marker_pda(value)[0], value)
        for value in ["ab#ab", "aa#bb", "a#b", "ab#b", "ab##ba"]:
            self.assertFalse(palindrome_marker_pda(value)[0], value)

if __name__ == "__main__":
    unittest.main()
