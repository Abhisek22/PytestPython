import pytest

@pytest.fixture(scope="session")
def basicSetup():
    print("This the basic setup method")
    yield
    print("Tearing down the setup to end everything")


@pytest.fixture(scope="class")
def ClassPreRequisite():
    print("This the Class Pre requisite setup method")