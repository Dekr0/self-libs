# ---------------------------------------------------
#   Name : Chengxuan Li
#   ID: 1631060
#   CMPUT 274, Fall 2020
#
#   Exercise 4: Text Preprocessor
# ---------------------------------------------------

from sys import argv


def arg_parse():
    """
    Receive and recognize an optional command line argument, mode, when the
    program is launch.

    :return: mode, the step doesn't need to perform
    """

    try:
        msg = "Correct usage: python3 preprocess.py <mode>\n" \
              "Optional argument, <mode>, can be one of three listed below\n" \
              "  - keep-digits, do not remove number from words\n" \
              "  - keep-stops, do not remove stopwords\n" \
              "  - keep-symbols, do not remove punctuation or symbols\n" \
              "If it is not provided, perform all the preprocess steps" \

        if not len(argv) > 2:
            mode = argv[1]
            if mode in ["keep-symbols", "keep-digits", "keep-stops"]:
                return mode

            quit("No such argument called \"{}\"\n".format(mode) + msg)

        quit("Too many optional arguments\n" + msg)

    except IndexError:
        return None


def main():
    """
    Main process / flow of this entire program

    :return:
    """
    mode = arg_parse()
    try:
        raw_txt = input()
        result = process(raw_txt, mode=mode)
        print(*result)
    except (EOFError, KeyboardInterrupt):
        quit()


def process(txt, mode):
    """
    Main process / flow of processing the list of words. Steps removing
    symbols, removing digits, removing stops are performed in order.

    :param txt: unprocessed text
    :param mode: step needed not to perform
    :return: a list of processed words
    """

    # Store the identifier of the functions into dictionary
    modes = {
        "keep-symbols": rm_symbols,
        "keep-digits": rm_digits,
        "keep-stops": rm_stops,
    }

    r_words = txt.lower().split()

    if not r_words:
        return []

    # If argument mode is provided, corresponding function identifier
    # will be remove, which means that the step will not perform
    if mode:
        del modes[mode]

    for func in modes.values():
        r_words = func(r_words)

    pro_words = r_words

    return pro_words


def rm_digits(words):
    """
    Remove all numbers unless the word consists only of numbers

    :param words: a list of unprocessed words
    :return: a list of processed words whose numbers are removed
    """

    for i in range(len(words)):
        if not all([char.isdigit() for char in words[i]]):
            words[i] = "".join([char for char in words[i]
                                if not char.isdigit()])

    return words


def rm_stops(words):
    """
    Remove all the stopwords from a list of words

    :param words: a list of unprocessed words
    :return: a list of words without stopwords
    """

    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves",
                 "you", "your", "yours", "yourself", "yourselves", "he",
                 "him", "his", "himself", "she", "her", "hers", "herself",
                 "it", "its", "itself", "they", "them", "their", "theirs",
                 "themselves", "what", "which", "who", "whom", "this", "that",
                 "these", "those", "am", "is", "are", "was", "were", "be",
                 "been", "being", "have", "has", "had", "having", "do", "does",
                 "did", "doing", "a", "an", "the", "and", "but", "if", "or",
                 "because", "as", "until", "while", "of", "at", "by", "for",
                 "with", "about", "against", "between", "into", "through",
                 "during", "before", "after", "above", "below", "to", "from",
                 "up", "down", "in", "out", "on", "off", "over", "under",
                 "again", "further", "then", "once", "here", "there",
                 "when", "where", "why", "how", "all", "any", "both",
                 "each", "few", "more", "most", "other", "some", "such",
                 "no", "nor", "not", "only", "own", "same", "so", "than",
                 "too", "very", "s", "t", "can", "will", "just", "don",
                 "should", "now"]

    p_word = [word for word in words if word not in stopwords]

    return p_word


def rm_symbols(words):
    """
    Remove all the symbols and punctuations in the word

    :param words:
    :return: a list of processed words whose punctuations and symbols
    are removed
    """

    for i in range(len(words)):
        words[i] = "".join([char for char in words[i] if char.isalnum()])

    return words


if __name__ == "__main__":
    main()
