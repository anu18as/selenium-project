# any pytest file name should start with test_ or end with _test
# pytest methods name should  start with test
# any code should wrapped in method only
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_Greet():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

