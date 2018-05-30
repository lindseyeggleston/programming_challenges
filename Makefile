.PHONY: test1
test1:
	py.test tests/unittests_challenge1.py
	py.test --pep8 src/challenge1.py

.PHONY: test2
test2:
	py.test tests/unittests_challenge2.py
	py.test --pep8 src/challenge2.py

.PHONY: test3
test3:
	py.test tests/unittests_challenge3.py
	py.test --pep8 src/challenge3.py
