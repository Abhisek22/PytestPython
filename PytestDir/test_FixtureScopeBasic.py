import pytest



#Declaring a method with pytest Fixture annotation
#defining scope of fixture as 'Function', 'Module', 'Class, 'Session'
#If no scope is mentioned to the fixture then by default it considers scope to be 'Function'
#Function scope will make the fixture method to run before each Test methods in pytest
#Module scope will make the fixture method to run once before executing the other test methods inside the file

@pytest.fixture(scope="module")
def preSetup():
    print("This the pre setup method")
@pytest.mark.regression
def test_firstTestMethod(preSetup):
    print("This is the First Test Method to Print")
def test_secondTestMethod(preSetup):
    print("This is the Second Test Method to Print")
