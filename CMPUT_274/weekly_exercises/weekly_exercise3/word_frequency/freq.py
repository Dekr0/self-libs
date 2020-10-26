# ---------------------------------------------------
#   Name : Chengxuan Li
#   ID: 1631060
#   CMPUT 274, Fall 2020
#
#   Exercise 3: Word Frequency
# ---------------------------------------------------


from os.path import exists
from sys import argv


def arg_parse():
    """
    Obtain the name of an input file from command arguments
    :return: filename - the name of an input file
    """
    if not len(argv) == 2:
        msg = "Too many" if len(argv) > 2 else "Too few"
        quit("%s command-line arguments\nValid command-line arguments: python3 freq.py filename" % msg)

    filename = argv[1]

    return filename


def count_word(words_list):
    """
    Analyze the word list to count the number of times each word appears in the
    text
    :param words_list:
    :return: a list of individual, space-separated words, and total words
    """
    total = len(words_list)

    # Create a dictionary to store and track the counts (the order of keys is already sorted in lexicographic order)
    words_count = dict().fromkeys(sorted(set(words_list)))

    for word in words_count.keys():
        words_count[word] = words_list.count(word)

    return words_count, total


def fetch_words(fin):
    """
    Read the contents of the file and divide the text into a list of individual,
    space-separated words
    :param fin: file object of an input file
    :return: a list of individual, space-separated words
    """
    words_list = fin.read().strip().split()
    fin.close()

    return words_list


def open_file(filename, mode="r"):
    """
    Open and create a file object
    :param filename: the name of an input / output file
    :param mode: open the file in a specific mode
    :return: a file object
    """
    if exists(filename) and mode == "r":
        fin = open(filename, mode)
        return fin
    elif mode == "w":
        fout = open(filename, mode)
        return fout

    quit("No such \"%s\" file exists" % filename)


def frequency_table(fout, result, total):
    """
    Write a frequency table of each, its count, and its relative frequency to an output file
    :param fout: a file object of the output file
    :param result: dictionary that store all the words and track their counts
    :param total: total words
    :return: None
    """
    for word, count in result.items():
        fout.write("%s %d %s\n" % (word, count, round(count / total, 3)))

    fout.close()


def main():
    filename = arg_parse()
    fin = open_file(filename)
    words_list = fetch_words(fin)
    result, total = count_word(words_list)
    fout = open_file(filename + ".out", mode="w")
    frequency_table(fout, result, total)


if __name__ == "__main__":
    main()
