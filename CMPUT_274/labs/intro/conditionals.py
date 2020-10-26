import sys

if __name__ == "__main__":
    try:
        x = int(sys.argv[1])
        if x > 0:
            print("Positive\n")
        elif x == 0:
            print("Zero\n")
        else:
            print("Negative\n")
    except ValueError:
        sys.exit("Invalid data type")

