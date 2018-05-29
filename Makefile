.PHONY: one
practice:
	py.test test/unittests_challenge1.py
	py.test --pep8 challenge1.py

.PHONY: two
practice:
	py.test test/unittests_challenge2.py
	py.test --pep8 challenge2.py

.PHONY: three
practice:
	py.test test/unittests_challenge3.py
	py.test --pep8 challenge3.py
