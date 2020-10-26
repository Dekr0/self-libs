from random import randint

if __name__ == "__main__":
    outcome = ['a', 'b', 'c', 'd', 'e', 'f']
    number = randint(1, len(outcome))
    print(outcome[number-1])
