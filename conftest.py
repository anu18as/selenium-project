import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will execute at last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["rahul","shetty","rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","Rahul"),("firefox","shetty"),"IE"])
def crossBrowser(request):
    return request.param