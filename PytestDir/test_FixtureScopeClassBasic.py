import pytest


@pytest.mark.usefixtures("ClassPreRequisite")
class Test_setup:

    def test_fifthTestMethod(self):
        print("This is the fifth Test Method to Print")

    def test_sixthTestMethod(self):
        print("This is the sixth Test Method to Print")