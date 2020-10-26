if __name__ == "__main__":
    total = 0
    while True:
        try:
            words = input("Word: ")  
            total += words.count("The") + words.count("the")
        except (EOFError, KeyboardInterrupt):
            print("")
            break
        finally:
            print("Total count: %d" % total)
