words = ['dog', 'mouse', 'cat']
print("The contents of obeject {} are {}".format(id(words), words))

words.sort()
print("The contents of object {} have been sorted to {}".format(id(words), words))

if "dog" in words:
    words.remove("dog")
    print("\"dog\" has been removed from the word list: {}".format(words))

numbers = [11, 25, 32, 4, 67, 18, 50, 11, 4, 11]
firstNum = numbers.pop(0)
print("The first value, %d, has been removed from the numbers list." % firstNum)

print("The value {} now appears in the number list {} times: {}".format(firstNum, numbers.count(firstNum), numbers))
