*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  aaa
    Set Password  passpass
    Enter Details
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  passpass
    Enter Details
    Register Should Fail With Message  Username must be at least

Register With Valid Username And Too Short Password
    Set Username  aaa
    Set Password  passpas
    Enter Details
    Register Should Fail With Message  Password must be at least

Register With Username That Is Already In Use
    Create User  aaa  helloworld
    Set Username  aaa
    Set Password  passpass
    Enter Details
    Register Should Fail With Message  Username already taken

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page

Enter Details
    Click  button >> text=Register
