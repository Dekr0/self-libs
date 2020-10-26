t1:
	python3 preprocess.py <<< "I need some help!"
	python3 preprocess.py <<< "I am feeling fine."
	python3 preprocess.py <<< "I was born in 1968!"
	python3 preprocess.py <<< ""
t2:
	python3 preprocess.py keep-digits <<< "I was born in 1968! This is 4real"
	python3 preprocess.py keep-stops <<< "I was born in 1968! This is 4real"
	python3 preprocess.py keep-symbols <<< "I was born in 1968! This is 4real"
	python3 preprocess.py keep-digits <<< ""
	python3 preprocess.py keep-stops <<< ""
	python3 preprocess.py keep-symbols <<< ""
	python3 preprocess.py keep-symbols <<< "4i hello"
	python3 preprocess.py keep-digits <<< "!i hello4"
	python3 preprocess.py keep-stops <<< "4i hello"
	python3 preprocess.py keep-stops <<< "i! hello"

	python3 preprocess.py <<< "I was born in 1968! This is 4real"
	python3 preprocess.py keep-number <<< "I was born in 1968! This is 4real"
