import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("i will execute fixtureDemo Method")

    def test_fixtureDemo1(self):
        print("i will execute fixtureDemo Method")

    def test_fixtureDemo2(self):
        print("i will execute fixtureDemo Method")

    def test_fixtureDemo3(self):
        print("i will execute fixtureDemo Method")
