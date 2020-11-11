# ---------------------------------------------------
#   Name : Chengxuan Li
#   ID: 1631060
#   CMPUT 274, Fall 2020
#
#   Assignment 1: OO Classifier
# ---------------------------------------------------
# Copyright 2020 Paul Lu


import sys
import copy     # for deepcopy()


Debug = False   # Sometimes, print for debugging
InputFilename = "file.input.txt"
TargetWords = [
        'outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow',
        'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots',
        'sunny', 'windy', 'coming', 'perfect', 'need', 'sun', 'on', 'was',
        '-40', 'jackets', 'wish', 'fog', 'pretty', 'summer'
        ]


def open_file(filename=InputFilename):
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)


def safe_input(f=None, prompt=""):
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            assert not (f is None)
            assert (f is not None)
            line = f.readline()
            if Debug:
                print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF")
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


class C274:
    def __init__(self):
        self.type = str(self.__class__)
        return

    def __str__(self):
        return(self.type)

    def __repr__(self):
        s = "<%d> %s" % (id(self), self.type)
        return(s)


class ClassifyByTarget(C274):
    def __init__(self, lw=[]):
        # FIXME:  Call superclass, here and for all classes
        self.type = str(self.__class__)
        self.allWords = 0
        self.theCount = 0
        self.nonTarget = []
        self.set_target_words(lw)
        self.initTF()
        return

    def initTF(self):
        self.TP = 0
        self.FP = 0
        self.TN = 0
        self.FN = 0
        return

    def get_TF(self):
        return(self.TP, self.FP, self.TN, self.FN)

    # FIXME:  Use Python properties
    #     https://www.python-course.eu/python3_properties.php
    def set_target_words(self, lw):
        # Could also do self.targetWords = lw.copy().  Thanks, TA Jason Cannon
        self.targetWords = copy.deepcopy(lw)
        return

    def get_target_words(self):
        return(self.targetWords)

    def get_allWords(self):
        return(self.allWords)

    def incr_allWords(self):
        self.allWords += 1
        return

    def get_theCount(self):
        return(self.theCount)

    def incr_theCount(self):
        self.theCount += 1
        return

    def get_nonTarget(self):
        return(self.nonTarget)

    def add_nonTarget(self, w):
        self.nonTarget.append(w)
        return

    def print_config(self):
        print("-------- Print Config --------")
        ln = len(self.get_target_words())
        print("TargetWords Hardcoded (%d): " % ln, end='')
        print(self.get_target_words())
        return

    def print_run_info(self):
        print("-------- Print Run Info --------")
        print("All words:%3s. " % self.get_allWords(), end='')
        print(" Target words:%3s" % self.get_theCount())
        print("Non-Target words (%d): " % len(self.get_nonTarget()), end='')
        print(self.get_nonTarget())
        return

    def print_confusion_matrix(self, targetLabel, doKey=False, tag=""):
        assert (self.TP + self.TP + self.FP + self.TN) > 0
        print(tag+"-------- Confusion Matrix --------")
        print(tag+"%10s | %13s" % ('Predict', 'Label'))
        print(tag+"-----------+----------------------")
        print(tag+"%10s | %10s %10s" % (' ', targetLabel, 'not'))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'TP   ', 'FP   '))
        print(tag+"%10s | %10d %10d" % (targetLabel, self.TP, self.FP))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'FN   ', 'TN   '))
        print(tag+"%10s | %10d %10d" % ('not', self.FN, self.TN))
        return

    def eval_training_set(self, tset, targetLabel):
        print("-------- Evaluate Training Set --------")
        self.initTF()
        z = zip(tset.get_instances(), tset.get_lines())
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class()
            if lb == targetLabel:
                if cl:
                    self.TP += 1
                    outcome = "TP"
                else:
                    self.FN += 1
                    outcome = "FN"
            else:
                if cl:
                    self.FP += 1
                    outcome = "FP"
                else:
                    self.TN += 1
                    outcome = "TN"
            explain = ti.get_explain()
            print("TW %s: ( %10s) %s" % (outcome, explain, w))
            if Debug:
                print("-->", ti.get_words())
        self.print_confusion_matrix(targetLabel)
        return

    def classify_by_words(self, ti, update=False, tlabel="last"):
        inClass = False
        evidence = ''
        lw = ti.get_words()
        for w in lw:
            if update:
                self.incr_allWords()
            if w in self.get_target_words():    # FIXME Write predicate
                inClass = True
                if update:
                    self.incr_theCount()
                if evidence == '':
                    evidence = w            # FIXME Use first word, but change
            elif w != '':
                if update and (w not in self.get_nonTarget()):
                    self.add_nonTarget(w)
        if evidence == '':
            evidence = '#negative'
        if update:
            ti.set_class(inClass, tlabel, evidence)
        return(inClass, evidence)

    # Could use a decorator, but not now
    def classify(self, ti, update=False, tlabel="last"):
        cl, e = self.classify_by_words(ti, update, tlabel)
        return(cl, e)

class ClassifyByTopN(ClassifyByTarget):

    def __init__(self, lw=()):
        """
        invoke the __init__ method of its parent class

        :param lw:
        """

        super().__init__(lw)

    def target_top_n(self, tset, num=5, label=''):
        """
        Select the top "num" most frequent words from all of the words
        in all the training instances, and set to the new words list

        Note: it is possible for the number of target words to be larger
        than "num", due to ties in the counts

        :param tset: a particular training dataset
        :param num: first n-th most frequent words selected as new target words
        :param label: only account words in training instances based on given
        labels
        :return:
        """

        words_dict = dict()  # Store all the words' count

        # Store all the words' count in ascending order based on frequency
        words_freq = []

        # Count all the words in all the training instances
        for ti in tset.get_instances():
            if ti.get_label() == label:
                for w in ti.get_words():
                    if w not in words_dict.keys():
                        words_dict[w] = 1
                    else:
                        words_dict[w] += 1

        # Sort the count
        for w, c in sorted(words_dict.items(),
                           key=lambda item: item[1], reverse=True):
            words_freq.append((w, c))


        i = 0  # A temporaily variable acts an index of words_freq

        # A flag variable to make sure that first n-th most frequent words
        # are selected
        n = 0

        top_n = []

        # Collect the first top n-th most frequent words and words with
        # tied counts
        while n < num:
            top_n.append(words_freq[i][0])

            # A temporarily list that stored the words with ties count
            words = []

            while True:
                if words_freq[i][1] != words_freq[i+1][1]:
                   i += 1
                   top_n += words # Append the words with tied counts
                   break
                words.append(words_freq[i+1][0])
                i += 1
                n += 1

                # Avoid the situation of which all the words in all the training
                # instances will be target words due to tie counts
                if i+1 == len(words_freq):
                    top_n.pop()
                    break

            n += 1

        self.set_target_words(top_n)


class TrainingInstance(C274):

    def __init__(self):
        self.type = str(self.__class__)
        self.inst = dict()
        # FIXME:  Get rid of dict, and use attributes
        self.inst["label"] = "N/A"      # Class, given by oracle
        self.inst["words"] = []         # Bag of words
        self.inst["class"] = ""         # Class, by classifier
        self.inst["explain"] = ""       # Explanation for classification
        self.inst["experiments"] = dict()   # Previous classifier runs
        return

    def get_label(self):
        return(self.inst["label"])

    def get_words(self):
        return(self.inst["words"])

    def set_class(self, theClass, tlabel="last", explain=""):
        # tlabel = tag label
        self.inst["class"] = theClass
        self.inst["experiments"][tlabel] = theClass
        self.inst["explain"] = explain
        return

    def get_class_by_tag(self, tlabel):             # tlabel = tag label
        cl = self.inst["experiments"].get(tlabel)
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_explain(self):
        cl = self.inst.get("explain")
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_class(self):
        return self.inst["class"]

    def process_input_line(
                self, line, run=None,
                tlabel="read", inclLabel=True
            ):
        for w in line.split():
            if w[0] == "#":
                self.inst["label"] = w
                # FIXME: For testing only.  Compare to previous version.
                if inclLabel:
                    self.inst["words"].append(w)
            else:
                self.inst["words"].append(w)

        if not (run is None):
            cl, e = run.classify(self, update=True, tlabel=tlabel)
        return(self)

    def preprocess_words(self, mode=""):
        """
        processing the list of words of current training instance.
        Steps removing symbols, removing digits, removing stops are performed
        in order.

        :param mode: step needed not to perform
        :return: None
        """

        # Store the identifier of the functions into dictionary
        modes = {
            "keep-symbols": self.rm_symbols,
            "keep-digits": self.rm_digits,
            "keep-stops": self.rm_stops,
        }

        self.inst["words"] = [w.lower() for w in self.get_words()]
        if not self.get_words():
            return

        # If argument mode is provided, corresponding function identifier
        # will be remove, which means that the step will not perform
        if mode:
            # If mode provided does not exist, raise an error
            assert mode in modes.keys(), "{} mode does not exist".format(mode)
            del modes[mode]

        for func in modes.values():
            func()

        return

    def rm_digits(self):
        """
        Remove all numbers unless the word consists only of numbers

        :return:  None
        """

        for i in range(len(self.get_words())):
            if not all([char.isdigit() for char in self.get_words()[i]]):
                self.inst["words"][i] = \
                    "".join([char for char in self.get_words()[i]
                             if not char.isdigit()])

        return

    def rm_stops(self):
        """
        Remove all the stopwords from a list of words

        :return: None
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

        self.inst["words"] = [word for word in self.get_words()
                              if word not in stopwords]

        return

    def rm_symbols(self):
        """
        Remove all the symbols and punctuations in the word

        :return: None
        """

        for i in range(len(self.get_words())):
            self.inst["words"][i] = \
                "".join([char for char in self.get_words()[i]
                         if char.isalnum()])

        return


class TrainingSet(C274):

    def __init__(self):
        self.type = str(self.__class__)
        self.inObjList = []     # Unparsed lines, from training set
        self.inObjHash = []     # Parsed lines, in dictionary/hash
        return

    def add_fold(self, tset):
        """
        Add the training instances from a provided training set into an current
        training set (object of class TrainingSet)

        :param tset: the training set whose training instances will be added into
        the current training set
        :return:
        """

        for ti in tset.get_instances():
            self.inObjHash.append(copy.deepcopy(ti))

        self.inObjList += tset.get_lines()

        return

    def copy(self):
        """
        Return a deepcopy of an object of class TrainingSet that contains
        the same attributes as the original object of class TrainingSet

        :return:
        """
        return (copy.deepcopy(self))

    def get_instances(self):
        return(self.inObjHash)      # FIXME Should protect this more

    def get_lines(self):
        return(self.inObjList)      # FIXME Should protect this more

    def print_training_set(self):
        print("-------- Print Training Set --------")
        z = zip(self.inObjHash, self.inObjList)
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class_by_tag("last")     # Not used
            explain = ti.get_explain()
            print("( %s) (%s) %s" % (lb, explain, w))
            if Debug:
                print("-->", ti.get_words())
        return

    def process_input_stream(self, inFile, run=None):
        assert not (inFile is None), "Assume valid file object"
        cFlag = True
        while cFlag:
            line, cFlag = safe_input(inFile)
            if not cFlag:
                break
            assert cFlag, "Assume valid input hereafter"

            # Check for comments
            if line[0] == '%':  # Comments must start with %
                continue

            # Save the training data input, by line
            self.inObjList.append(line)
            # Save the training data input, after parsing
            ti = TrainingInstance()
            ti.process_input_line(line, run=run)
            self.inObjHash.append(ti)
        return

    def preprocess(self, mode=""):
        """
        Perform preprocessing for all training instances in a particular training dataset

        :param mode: step needed not to perform
        :return: None
        """

        for ti in self.get_instances():
            ti.preprocess_words(mode)
        return

    def return_nfolds(self, num=3):
        """
        Returns "num" objects of class TrainingSet. Each of the objects
        returned contains a partition or fold of the original training dataset.

        :param num: determine the number of objects of class TrainingSet returned
        or "num" folds for cross validation
        :return: "num" objects of class TrainingSet with partitions or folds of
        the original training dataset
        """

        # List that contains "num" objects of class TrainingSet
        folds = [TrainingSet() for i in range(num)]

        # Divided whole training dataset into n different folds using round robin
        # strategy
        for i in range(len(self.get_instances())):
            folds[i % num].inObjHash.append \
                (copy.deepcopy(self.get_instances()[i]))  # training instances

            # actual (string) sentences from the training instances
            folds[i % num].inObjList.append(self.get_lines()[i])

        return folds

def basemain():
    tset = TrainingSet()
    run1 = ClassifyByTarget(TargetWords)
    print(run1)     # Just to show __str__
    lr = [run1]
    print(lr)       # Just to show __repr__

    argc = len(sys.argv)
    if argc == 1:   # Use stdin, or default filename
        inFile = open_file()
        assert not (inFile is None), "Assume valid file object"
        tset.process_input_stream(inFile, run1)
        inFile.close()
    else:
        for f in sys.argv[1:]:
            inFile = open_file(f)
            assert not (inFile is None), "Assume valid file object"
            tset.process_input_stream(inFile, run1)
            inFile.close()

    if Debug:
        tset.print_training_set()
    run1.print_config()
    run1.print_run_info()
    run1.eval_training_set(tset, '#weather')

    return


if __name__ == "__main__":
    basemain()
