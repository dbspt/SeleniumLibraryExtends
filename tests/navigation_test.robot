*** Settings ***
Documentation       Tests navigation

Library             SeleniumLibrary
Library             SeleniumLibraryExtends

Test Teardown   Close browser

*** Test Cases ***
Open Browser
    [Documentation]     Open browser chrome.
    I open the browser chrome

Navigate to
    [Documentation]     Navigate to Google.
    I open the browser chrome
    I am on https://www.google.com.br
    Title Should Be        Google

Back navigation
    [Documentation]     Back navigation.
    I open the browser chrome
    I am on https://www.google.com.br
    Title Should Be        Google
    I am on https://www.youtube.com
    Title Should Be        YouTube
    I navigate back
    Title Should Be        Google

Get title
    [Documentation]     Get title.
    I open the browser chrome
    I am on https://www.google.com.br
    ${title}=    I retrieve the page title
    Title Should Be        ${title}