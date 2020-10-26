def safe_input(prompt):
    try:
        line = input(prompt)
        return (line, True)
    except EOFError:
        return ("", False)


if __name__ == "__main__":
    flag = True
    while flag:
        words, flag = safe_input("")
        for w in words.split():
            print(w)

