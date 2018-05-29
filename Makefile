.PHONY: one
one:
	py.test tests/unittests_challenge1.py
	py.test --pep8 challenge1.py

.PHONY: two
two:
	py.test tests/unittests_challenge2.py
	py.test --pep8 challenge2.py

.PHONY: three
three:
	py.test tests/unittests_challenge3.py
	py.test --pep8 challenge3.py
