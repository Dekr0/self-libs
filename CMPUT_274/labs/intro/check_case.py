if __name__ == "__main__":
    inp = input("Input something: ").strip()
    if inp:
        if inp[0].isupper() and inp[len(inp)-1].islower():
            print("Yes")
        else:
            print("No")
    else:
        print("Invalid Input")
    
