import pytest


@pytest.mark.regression
def test_thirdTestMethod(basicSetup):
    print("This is the third Test Method to Print")

def test_fourthTestMethod(basicSetup):
    print("This is the fourth Test Method to Print")