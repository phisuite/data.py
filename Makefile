PYTHON_VERSION?=3.8.1
PYTHON?=~/.pyenv/versions/${PYTHON_VERSION}/bin/python
REPO?=pypi

compile:
	${PYTHON} setup.py sdist bdist_wheel

publish:
	${PYTHON} -m twine upload -r ${REPO} dist/*

clean:
	rm -r build dist *.egg-info

install:
	${PYTHON} -m pip install --user --upgrade setuptools wheel twine
