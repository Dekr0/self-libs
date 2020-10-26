if __name__ == "__main__":
    try:
        numf = float(input(">>> ").strip())
        print(int(numf) if not numf % 1 else numf)
    except ValueError:
        print("Invalid Input")
