if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    result = 0
    while n != 0:
        result += 1/n
        n -= 1
    print(result)
