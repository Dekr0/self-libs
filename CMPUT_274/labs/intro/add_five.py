if __name__ == "__main__":
    try:
        print(int(input("Enter an integer: ".strip()))+5)
    except ValueError:
        print("Invalid Input")
