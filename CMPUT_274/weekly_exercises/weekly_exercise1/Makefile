all: testcase

testcase:
	for testcase in $(shell find $(testcases) -name '*.txt'); do \
		cat $$testcase; \
		python3 validator.py <  $$testcase; \
		echo; \
	done

