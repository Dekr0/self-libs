if __name__ == "__main__":
    inp = input("Input something: ").strip()
    if inp:
        print(inp if len(inp) == 1 else inp[0] + inp[len(inp)-1])
    else:
        print("Empty Input")
