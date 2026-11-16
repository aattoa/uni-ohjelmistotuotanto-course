*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kalle
    Set Password  kalle123
    Enter Details
    Login Should Succeed

Login With Incorrect Password
    Set Username  kalle
    Set Password  kalle456
    Enter Details
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  veryrealhuman
    Set Password  veryrealpassword
    Enter Details
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Login Page
    Reset Application
    Create User  kalle  kalle123
    Go To Login Page

Enter Details
    Click  button >> text=Login
