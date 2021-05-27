# [Pytest](https://docs.pytest.org) is a testing framework.


## To Enable Pytest for your project
Open the Settings/Preferences | Tools | Python Integrated Tools settings dialog as described in Choose your testing framework.

In the Default test runner field select pytest.

Click OK to save the settings.

Install pytest through `pip3 install pytest`

## To run the Unit Tests

pytest -v -s Path of Project
`pytest -v -s /Users/pytest/pack`

pytest -v -s <FileName.py>

1. `py.test -v -s runner.py workflow.py`
2. `py.test -v -s runner.py workflow.py`

pytest -v -s <FileName.py>::<method_name>
 `py.test -v -s runner.py::test_anshu_test`