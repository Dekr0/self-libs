def safe_input(prompt):
    try:
        words = input(prompt).split()
        return (words, True)
    except EOFError:
        return ("", False)


if __name__ == "__main__":
    theCount = 0
    allWords = 0
    nonTarget = []
    flag = True
    while flag:
        words, flag = safe_input("")
        if flag:
            allWords += len(words)
            for word in words:
                if word in ['the', 'The']:
                    theCount += 1
                    continue
                nonTarget.append(word)
            

print("All words: %3s. Target words: %3s" % (allWords, theCount))
print("Non-Target words: ", nonTarget)
