if __name__ == "__main__":
    a = input("Enter first string: ").strip()
    b = input("Enter second string: ").strip()
    output = "{} is longer than {}"
    if len(a) == len(b):
        print("The strings are the same length")
    elif len(a) > len(b):
        print(output.format(a,b))
    else:
        print(output.format(b,a))
