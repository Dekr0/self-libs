if __name__ == "__main__":
    try:
        print(abs(float(input("Enter a number:").strip())))
    except ValueError:
        print("Invalid Input")
