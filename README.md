# simple_tests
Simple Python unit tests and coverage report

All commands moving forward assume you are the `root` directory

## Install Coverage.py
Run this command to install Coverage.py: `pip install coverage`

Verify installation: `coverage --version`

Expected Output:
```
Coverage.py, version 6.3.2 with C extension
Full documentation is at https://coverage.readthedocs.io
```

Read Coverage.py docs here: https://coverage.readthedocs.io/en/6.3.2/index.html

## [Optional] Run sample code 
Run this command:
`python3 ./src/main.py`

Output:
```
What is your name? Super Code
Hi, Super Code
```

## Run Coverage.py
The Python `unittest` module is used to structure the tests found in the `tests` directory. 
Read about `unittest` here: https://docs.python.org/3/library/unittest.html

Coverage.py is a tool for measuring code coverage in Python programs. 
Run this command to execute Coverage.py in this project:
```
coverage run -m unittest tests/*_test.py
```
Output:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
The command dissected where `[MODULE] = unittest` and `[TEST FILE(S)] = tests/*_test.py`
```
coverage run -m [MODULE] [TEST FILE(S)]
```

## Coverage.py report
To get the Coverage.py report, run:
```
coverage report
```
Output:
```
Name                                                                 Stmts   Miss  Cover
----------------------------------------------------------------------------------------
/usr/local/lib/python3.9/site-packages/_distutils_hack/__init__.py      92     87     5%
src/main.py                                                              5      0   100%
tests/main_test.py                                                      17      0   100%
----------------------------------------------------------------------------------------
TOTAL                                                                  114     87    24%
```
To get a HTML-friendly version of the report, run:
```
coverage html
```
Output:
```
Wrote HTML report to htmlcov/index.html
```