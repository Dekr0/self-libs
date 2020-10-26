if __name__ == "__main__":
    total = 0
    while True:
        word = input("Word: ")  
        if word == "the":
            total += 1
        elif word == "The":
            total += 1
        print("Total count: %d" % total)
        if word == "exit":
            break
