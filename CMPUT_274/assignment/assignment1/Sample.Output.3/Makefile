alltest:
	make test1
	make test2
	make test3

output:
	make test1 > output.1
	make test2 > output.2
	make test3 > output.3
	diff output.1 data.v1.correct.output.v3
	diff output.2 helpdata.v1.correct.output.v3
	diff output.3 driverdata.v1.correct.output.v3
# This test is supposed to do something sensible with the data and
#	the new methods.  Read the comments in the code.
#
#    # FIXME Flaw in ooclassifier.py means that we need to drop
#    #   the most frequent target word if it is also the positive label
test1:
	python3 a1.alldriver.v3.py data.v1

# This test is supposed to do something sensible with the data and
#	the new methods.  Read the comments in the code.
#
#    # FIXME Flaw in ooclassifier.py means that we need to drop
#    #   the most frequent target word if it is also the positive label
test2:
	python3 a1.alldriver.v3.py helpdata.v1

# This is a nonsense test because of the input data,
#	just to provide another output example by which to compare.
test3:
	python3 a1.alldriver.v3.py driverdata.v1

clean:
	-/bin/rm -r -f __pycache__
	rm output.?
