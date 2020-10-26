if __name__ == "__main__":
    try:
        raw = input("Enter numbers (separate with single space): ")
        print(list(map(float, raw.split())))
        print([float(x) for x in raw.split()])
    except ValueError:
        print("Invalid Input")
