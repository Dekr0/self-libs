if __name__ == "__main__":
    while True:
        inp = input("Enter a word: ")
        count = inp.count("The") + inp.count("the")
        print("The number of times word \"The\" or \"the\" occurs: {}".format(count))

