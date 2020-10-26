def safe_input(prompt):
    try:
        words = input(prompt).split()
        return (words, True)
    except EOFError:
        return ("", False)
