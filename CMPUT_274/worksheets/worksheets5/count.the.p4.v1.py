def safe_input(prompt):
    try:
        word = input(prompt)
        return (word, True)
    except EOFError:
        return ("", False)


if __name__ == "__main__":
    theCount = 0
    allWords = 0
    nonTarget = []
    flag = True
    while flag:
        word, flag = safe_input("")
        if flag:
            allWords += 1
        if word in ['the', 'The']:
            theCount += 1
        elif word != '':
            if word not in nonTarget:
                nonTarget.append(word)
print("All words: %3s. Target words: %3s" % (allWords, theCount))
print("Non-Target words: ", nonTarget)
