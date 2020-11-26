# Copyright 2020 Paul Lu
# This code is only intended to show one way in which the new methods
#   from Task II can be called.  For a more meaningful classification
#   driver, look in:  a1.alldriver.v1.py
#
import sys
import copy     # for deepcopy()

# What we might do to test your code
# from ooclassifier import *
# from ooclassifierbase import *
from ooclassifierbasev4 import *

Debug = False   # Sometimes, print for debugging

class ClassifyByTopN(ClassifyByTarget):
    def __init__(self, lw=[]):
        self.type = str(self.__class__)
        super().__init__(lw)
        return

    #   Compare with classify_all() in class TrainingSet
    def classify_all(self, ts, update=True, tlabel="classify_all"):
        for ti in ts.get_instances():
            cl, e = self.classify(ti, update=update, tlabel=tlabel)
        return

    # *********************************************
    # Task II placeholder
    # *********************************************
    def target_top_n(self, tset, num=5, label=''):
        # Assumes class TrainingInstance has preprocess_words()
        # Task II FIXME Placeholder
        self.set_target_words(['the', 'snow', 'well', 'weather', 'dizzy'])
        return


class NewTrainingSet(TrainingSet):
    def __init__(self):
        self.type = str(self.__class__)
        super().__init__()
        self.variable = dict()
        return

    def set_env_variable(self, k, v):
        self.variable[k] = v
        return

    def get_env_variable(self, k):
        if k in self.variable:
            return(self.variable[k])
        else:
            return ""

    def inspect_comment(self, line):
        if len(line) > 1 and line[1] != ' ':      # Might be variable
            v = line.split(maxsplit=1)
            self.set_env_variable(v[0][1:], v[1])
        return

    # *********************************************
    # Task I placeholder.  Should really be placed in class TrainingSet
    # *********************************************
    def preprocess(self, mode=''):
        # Assumes class TrainingInstance has preprocess_words()
        return

    def process_input_stream(self, inFile, run=None):
        assert not (inFile is None), "Assume valid file object"
        cFlag = True
        while cFlag:
            line, cFlag = safe_input(inFile)
            if not cFlag:
                break
            assert cFlag, "Assume valid input hereafter"

            # NEW Lecture 16
            if len(line) == 0:   # Blank line.  Skip it.
                continue

            # Check for comments
            if line[0] == '%':  # Comments must start with %
                # NEW Lecture 15
                self.inspect_comment(line)
                continue

            # Save the training data input, by line
            self.inObjList.append(line)
            # Save the training data input, after parsing
            ti = TrainingInstance()
            ti.process_input_line(line, run=run)
            self.inObjHash.append(ti)
        return


def main():
    # NEW Use our new subclasses
    tset = NewTrainingSet()
    run1 = ClassifyByTopN()

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

    print("--------------------------------------------")
    pfeatures = tset.get_env_variable("pos-features")
    print("pos-features: ", pfeatures)
    plabel = tset.get_env_variable("pos-label")
    print("pos-label: ", plabel)
    print("--------------------------------------------")

    # Do the classification per environment variables of input
    run1.set_target_words(pfeatures.strip().split())  # FIXME Could be cleaner
    run1.classify_all(tset)
    run1.print_config()
    run1.eval_training_set(tset, plabel)

    # *********************************************
    # *** Look here *** for Task II
    # *********************************************
    run1.target_top_n(tset, num=5, label=plabel)  # Call to new Task II method
    run1.classify_all(tset)     # Redo the classification
    run1.print_config()         # Print New config and evaluation
    run1.eval_training_set(tset, plabel)

    tp, fp, tn, fn = run1.get_TF()
    precision = float(tp) / float(tp + fp)
    recall = float(tp) / float(tp + fn)
    accuracy = float(tp + tn) / float(tp + tn + fp + fn)
    print("Accuracy:  %3.2g = " % accuracy, end='')
    print("(%d + %d) / (%d + %d + %d + %d)" % (tp, tn, tp, tn, fp, fn))
    print("Precision: %3.2g = " % precision, end='')
    print("%d / (%d + %d)" % (tp, tp, fp))
    print("Recall:    %3.2g = " % recall, end='')
    print("%d / (%d + %d)" % (tp, tp, fn))
    return


if __name__ == "__main__":
    main()
