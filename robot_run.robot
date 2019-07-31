*** Settings ***
Library    RobotLibrary.py

*** Test Cases ***
My Test
    run_positive_test_case_yahoo_transit
    run_negative_test_case_login_error


#*** Settings ***
# For python 3, use robot instead of pybot (my python version is 3.7.2)
# https://stackoverflow.com/questions/48134803/calling-a-method-which-is-inside-a-class-in-python-from-a-robot-file
#Library    MyLibrary
#
#*** Test Cases ***
#My Test
#    Do Nothing
#    Hello    world
#    
#    
#    
#Keyword names
#Keyword names used in the test data are compared with method names to find the method implementing these keywords. Name comparison is case-insensitive, and also spaces and underscores are ignored. For example, the method hello maps to the keyword name :name:`Hello`, :name:`hello` or even :name:`h e l l o`. Similarly both the do_nothing and doNothing methods can be used as the :name:`Do Nothing` keyword in the test data.
#
#Example Python library implemented as a module in the :file:`MyLibrary.py` file:
#
#def hello(name):
#    print("Hello, %s!" % name)
#
#def do_nothing():
#    pass
#
#*** Settings ***
#Documentation    Example using the space separated plain text format.
#Library          OperatingSystem
#
#*** Variables ***
#${MESSAGE}       Hello, world!
#
#*** Test Cases ***
#My Test
#    [Documentation]    Example test
#    Log    ${MESSAGE}
#    My Keyword    /tmp
#
#Another Test
#    Should Be Equal    ${MESSAGE}    Hello, world!
#
#*** Keywords ***
#My Keyword
#    [Arguments]    ${path}
#    Directory Should Exist    ${path}
