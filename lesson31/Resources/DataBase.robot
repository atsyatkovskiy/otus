*** Settings ***
Library    DatabaseLibrary


*** Variables ***
${CUSTOMER_DB}    oc_customer


*** Keywords ***
Check User In Database
    [Arguments]    ${value}
    Check If Exists In Database    select * from ${CUSTOMER_DB} where firstname = '${value}[0]' and lastname = '${value}[1]'
