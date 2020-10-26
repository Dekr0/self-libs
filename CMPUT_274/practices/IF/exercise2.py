if __name__ == "__main__":
    sides = set(map(int, input("").split()))
    if len(sides) == 1:
        print("Equilatera")
    elif len(sides) == 2:
        print("Isoceles")
    else:
        print("Scalene")

