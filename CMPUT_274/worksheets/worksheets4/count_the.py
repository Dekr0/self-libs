if __name__ == "__main__":
    count = 0
    word = ""
    while word != "exit":
        word = input("Word: ")
        if word in ['the', 'The']:
            count += 1
        print("Total count %s" % count)

