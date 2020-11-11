alltest:
	make test1
	make test2
output:
	make test1 > output.1
	make test2 > output.2
	diff output.1 data.v1.correct.output
	diff output.2 helpdata.v1.correct.output
# This test is supposed to do something sensible with the data and
#	the new methods.  Read the comments in a1.alldriver.v1.py
#
#    # FIXME Flaw in ooclassifierbase.py means that we need to drop
#    #   the most frequent target word if it is also the positive label
test1:
	python3 a1.alldriver.v1.py data.v1

# This test is supposed to do something sensible with the data and
#	the new methods.  Read the comments in a1.alldriver.v1.py
#
#    # FIXME Flaw in ooclassifierbase.py means that we need to drop
#    #   the most frequent target word if it is also the positive label
test2:
	python3 a1.alldriver.v1.py helpdata.v1

# These test produce "nonsense" output.  They exist to show how
#	the new methods can be called.
driver:
	python3 a1.driver.1.py helpdata.v1
	python3 a1.driver.2.py helpdata.v1
	python3 a1.driver.3.py helpdata.v1
	python3 a1.driver.1.py data.v1
	python3 a1.driver.2.py data.v1
	python3 a1.driver.3.py data.v1

clean:
	-/bin/rm -r -f __pycache__
