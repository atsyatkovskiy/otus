*** Settings ***
Documentation    API Тесты

Library    RequestsLibrary


*** Variables ***
${API_URL}    https://jsonplaceholder.typicode.com/todos


*** Test Cases ***
Test Get Resource Positive
    [Template]    Get Resource
    1    200
    100    200
    200    200


Test Get Resource Negative
    [Template]    Get Resource
    -1    404
    0    404
    201    404
    None    404
    string    404


*** Keywords ***
Get Resource
    [Arguments]    ${todo_id}    ${status}
    Create Session    api_test    url=${API_URL}    disable_warnings=1
    ${resp}    GET On Session    api_test    /${todo_id}    expected_status=${status}
    Status Should Be    ${status}    ${resp}
