# This works if ooclassifier.py is complete and solves Tasks I, II, and III
from ooclassifier.ooclassifier import *

Debug = True   # Sometimes, print for debugging

# This class exists so that we can test code that is based on:
#       ooclassifier.py     (as released alongside Assignment #1)
#
# But, it should also work if one is using ooclassifierbasev4.py (or v3.py)
class NewTrainingSet(TrainingSet):
    def __init__(self):
        self.type = str(self.__class__)
        super().__init__()
        self.variable = dict()
        return

    # FIXME Put me into TrainingSet, after Assignment #1 is done
    def set_env_variable(self, k, v):
        self.variable[k] = v
        return

    # FIXME Put me into TrainingSet, after Assignment #1 is done
    def get_env_variable(self, k):
        if k in self.variable:
            return(self.variable[k])
        else:
            return ""

    # NEW NEW for the driver
    # FIXME Put me into TrainingSet, after Assignment #1 is done
    def remove_hashtags(self):
        for ti in self.get_instances():
            nw = []
            ow = ti.get_words()
            for w in ow:
                if w[0] != '#':
                    nw.append(w)
            # ti.set_words(nw)      # set_words() not in base yet, so...
            ti.inst["words"] = nw   # FIXME Minor hack
            if Debug:
                print("Before: ", ' '.join(ow))
                print("After : ", ' '.join(nw))
        return


    # FIXME Put me into TrainingSet, after Assignment #1 is done
    def inspect_comment(self, line):
        if len(line) > 1 and line[1] != ' ':      # Might be variable
            v = line.split(maxsplit=1)
            self.set_env_variable(v[0][1:], v[1])
        return

    # FIXME Put me into TrainingSet, after Assignment #1 is done
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


class NewClassifyByTopN(ClassifyByTopN):
    def __init__(self, lw=[]):
        self.type = str(self.__class__)
        super().__init__(lw)
        return

    # FIXME Put me into ClassifyXX, after Assignment #1 is done
    # Compare with classify_all() in class TrainingSet
    def classify_all(self, ts, update=True, tlabel="classify_all"):
        for ti in ts.get_instances():
            cl, e = self.classify(ti, update=update, tlabel=tlabel)
        return

    # FIXME Put me into ClassifyXX, after Assignment #1 is done
    def print_pra(self):
        tp, fp, tn, fn = self.get_TF()
        precision = float(tp) / float(tp + fp)
        recall = float(tp) / float(tp + fn)
        accuracy = float(tp + tn) / float(tp + tn + fp + fn)
        print("Accuracy:  %3.2g = " % accuracy, end='')
        print("(%d + %d) / (%d + %d + %d + %d)" % (tp, tn, tp, tn, fp, fn))
        print("Precision: %3.2g = " % precision, end='')
        print("%d / (%d + %d)" % (tp, tp, fp))
        print("Recall:    %3.2g = " % recall, end='')
        print("%d / (%d + %d)" % (tp, tp, fn))


def main():
    # NEW Use our new subclasses
    tset = NewTrainingSet()
    run1 = NewClassifyByTopN()

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

    # Save a copy of original training set
    tsetOrig = tset.copy()

    print("--------------------------------------------")
    pfeatures = tset.get_env_variable("pos-features")
    print("pos-features: ", pfeatures)
    plabel = tset.get_env_variable("pos-label")
    print("pos-label: ", plabel)

    # FIXME This now fixes the problem with positive labels as features
    tset.remove_hashtags()

    print("\n** Full Dataset (no preprocessing) *********")
    run1.target_top_n(tset, num=3, label=plabel)
    print(run1.get_target_words())
    run1.classify_all(tset)
    run1.print_config()
    run1.eval_training_set(tset, plabel)
    run1.print_pra()

    print("\n** Full Dataset (with preproc, top N) ******")
    tset.preprocess()
    run1.target_top_n(tset, num=3, label=plabel)
    print("Target Words: ", run1.get_target_words())
    run1.classify_all(tset)
    run1.print_config()
    run1.eval_training_set(tset, plabel)
    run1.print_pra()

    print("\nDoes preprocessing improve PRA? (Not 100% apples vs. oranges.)")

    print("\n** By folds (3) ****************************")

    # FIXME Should use loop, but keep it simple for clarity, for now

    # Create folds for cross-validation.  Not necessarily most efficient way..
    ts_3 = tset.return_nfolds(3)

    # Done this (inefficient) way to clearly show cross validation
    #   The following really shows off the encapsulation/ADT benefits of OO
    train0 = NewTrainingSet()
    test0 = NewTrainingSet()
    test0.add_fold(ts_3[0])
    train0.add_fold(ts_3[1])
    train0.add_fold(ts_3[2])

    train1 = NewTrainingSet()
    test1 = NewTrainingSet()
    train1.add_fold(ts_3[0])
    test1.add_fold(ts_3[1])
    train1.add_fold(ts_3[2])

    train2 = NewTrainingSet()
    test2 = NewTrainingSet()
    train2.add_fold(ts_3[0])
    train2.add_fold(ts_3[1])
    test2.add_fold(ts_3[2])

    print("   *** Using Test Fold 0 *******************")
    run1.target_top_n(train0, num=3, label=plabel)
    run1.classify_all(test0)
    run1.print_config()
    run1.eval_training_set(test0, plabel)
    run1.print_pra()

    print("   *** Using Test Fold 1 *******************")
    run1.target_top_n(train1, num=3, label=plabel)
    run1.classify_all(test1)
    run1.print_config()
    run1.eval_training_set(test1, plabel)
    run1.print_pra()

    print("   *** Using Test Fold 2 *******************")
    run1.target_top_n(train2, num=3, label=plabel)
    run1.classify_all(test2)
    run1.print_config()
    run1.eval_training_set(test2, plabel)
    run1.print_pra()
    return


if __name__ == "__main__":
    main()
