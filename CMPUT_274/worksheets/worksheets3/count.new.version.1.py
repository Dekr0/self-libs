if __name__ == "__main__":
    total = 0
    word = ""
    while word != "exit":
        word = input("Word: ")
        total += word.count("The") + word.count("the")
        print("Total count: %d" % total)

