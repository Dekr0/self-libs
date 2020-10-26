from random import *

if __name__ == "__main__":
    num = int(input("Enter a guess between 1 and 100: "))
    ans = randint(1,100)
    if num == ans:
        print("Correct guess")
    elif num > ans:
        print("Too high")
    else:
        print("Too low")
