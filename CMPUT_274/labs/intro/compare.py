if __name__ == "__main__":
    try:
        print(max(input("Enter two number (separated with comma): ").strip().split(",")))
    except:
        print("Invalid Input")
