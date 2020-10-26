Debug = False
InputObjectsList = []
InputObjectsHash = []
allWords = 0
theCount = 0
nonTarget = [] 
TargetWords = ['outside', 'today', 'weather', 'raining', 'nice' ]


Index = 0
FakeFile = [
        "#weather        nice weather eh",
        "#weather        snow is coming",
        "#weather        wind is high",
        "#negative       good food",
        "#negative       i need a coffee"
    ]


def open_file(filename=""):
    return(FakeFile)


def safe_input(f=None, prompt=""):
    global Index
    if Index < len(FakeFile):
        Index += 1
        return(FakeFile[Index-1], True)
    else:
        return("", False)


def print_training_data_obj(inObjList, inObjHash):
    i = 0
    while i < len(inObjList):
        print("( %s) %s" % (inObjHash[i]["label"], inObjList[i]))
        if Debug:
            print("-->", inObjHash[i]["words"])
        i += 1


def process_input_line(line):
    global allWords, theCount, nonTarget

    trainInstance = {}
    trainInstance["label"] = "None"
    trainInstance["words"] = []
    for w in line.split():
        allWords = allWords + 1
        if w[0] == "#":
            trainInstance["label"] = w
        else:
            trainInstance["words"].append(w)

        if w in TargetWords:
            theCount = theCount + 1
        elif w != '':
            if w not in nonTarget:
                nonTarget.append(w)
    return(trainInstance)


def process_input_stream(inFile, inObjList, inObjHash):
    assert not (inFile is None), "Assume valid file object"

    cFlag = True
    while cFlag:
        line, cFlag = safe_input(inFile)
        if not cFlag:
            break
        assert cFlag, "Assume valid input hereafter"
        inObjList.append(line)
        inObjHash.append(process_input_line(line))


def main():
    inFile = open_file()
    assert not (inFile is None), "Assume valid file object"

    process_input_stream(inFile, InputObjectsList, InputObjectsHash)
    # inFile.close()

    print("TargetWords Hardcoded (%d): " % len(TargetWords), TargetWords)
    print_training_data_obj(InputObjectsList, InputObjectsHash)

    print("All words:%3s. Target words:%3s" % (allWords, theCount))
    print("Non-Target words: ", nonTarget)


if __name__ == "__main__":
    main()


