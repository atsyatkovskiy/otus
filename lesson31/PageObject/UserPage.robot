*** Settings ***
Library    SeleniumLibrary
Library    DatabaseLibrary


*** Variables ***
${ACCOUNT_ICON}    css=#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md
${REGISTER_LINK}    xpath=//a[contains(@href, "register")]
${REGISTER_FORM}    id=content
${FIRST_NAME_INPUT}    id=input-firstname
${LAST_NAME_INPUT}    id=input-lastname
${EMAIL_INPUT}    id=input-email
${TEL_INPUT}    id=input-telephone
${PASSWORD_REGISTER}    id=input-password
${PASSWORD_CONFIRM_REGISTER}    id=input-confirm
${AGREE_CHECKBOX}    xpath=//input[@name="agree"]
${CONTINUE_BUTTON}    css=.btn.btn-primary
${SUCCESS_REGISTER_HEADER}    css=#content > h1


*** Keywords ***
Go To Register Form
    Wait Until Element Is Visible    ${ACCOUNT_ICON}
    Click Element    ${ACCOUNT_ICON}
    Click Element    ${REGISTER_LINK}
    Wait Until Element Is Visible     ${REGISTER_FORM}


Register New User
    [Arguments]  ${user_data}
    Input Text    ${FIRST_NAME_INPUT}    ${user_data}[0]
    Input Text    ${LAST_NAME_INPUT}    ${user_data}[1]
    Input Text    ${EMAIL_INPUT}    ${user_data}[2]
    Input Text    ${TEL_INPUT}    ${user_data}[3]
    Input Text    ${PASSWORD_REGISTER}    ${user_data}[4]
    Input Text    ${PASSWORD_CONFIRM_REGISTER}    ${user_data}[4]
    Click Element    ${AGREE_CHECKBOX}
    Click Element    ${CONTINUE_BUTTON}
    Wait Until Element Is Visible    ${SUCCESS_REGISTER_HEADER}
    ${SUCCESS_HEADER}    Get Text    ${SUCCESS_REGISTER_HEADER}
    Should Be Equal    ${SUCCESS_HEADER}    Your Account Has Been Created!
