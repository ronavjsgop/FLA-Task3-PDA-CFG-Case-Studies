from pda_cfg.cases import run_all, run_brackets, run_expression, run_palindrome

def main():
    import sys
    command = sys.argv[1].lower() if len(sys.argv) > 1 else "all"
    commands = {
        "all": run_all,
        "brackets": run_brackets,
        "expression": run_expression,
        "palindrome": run_palindrome,
    }
    if command not in commands:
        print("Usage: python main.py [all|brackets|expression|palindrome]")
        raise SystemExit(1)
    commands[command]()

if __name__ == "__main__":
    main()
