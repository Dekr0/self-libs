if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    result = 0
    for i in range(1,n+1):
        result += 1/i
    print(result)
