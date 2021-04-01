*** Settings ***
Library    SeleniumLibrary
Library    DatabaseLibrary


*** Variables ***
${LOGIN_FORM}    css=form
${LOGIN_USER_NAME_INPUT}    css=#input-username
${LOGIN_PASSWORD_INPUT}    css=#input-password
${LOGIN_BUTTON}    css=button[type='submit']
${LOGOUT_BUTTON}    css=#header > div > ul > li:nth-child(2) > a
${NAVIGATION_LIST}    css=#menu

@{ADD_BUTTON}   css=a.btn.btn-primary[data-original-title='Add New']
@{DEL_BUTTON}    css=button[data-original-title=Delete]

@{SAVE_BUTTON}    css=button[type=submit]
@{ALERT_SUCCESS}    css=div.container-fluid > div.alert.alert-success.alert-dismissible
@{MENU_CATALOG}    id=menu-catalog
@{MENU_CATALOG_CHILD}    css=#collapse1 > li > a

${USER}    user
${PASSWORD}    bitnami
${URL}    http://192.168.1.34/admin/

*** Keywords ***
Login admin user
    Go To    ${URL}
    Wait Until Element Is Visible    ${LOGIN_FORM}
    Input Text    ${LOGIN_USER_NAME_INPUT}  ${USER}
    Input Text    ${LOGIN_PASSWORD_INPUT}  ${PASSWORD}
    Submit Form    ${LOGIN_FORM}
    Wait Until Element Is Visible    ${NAVIGATION_LIST}

Logout admin user
    Wait Until Element Is Visible    ${LOGOUT_BUTTON}
    Click Element    ${LOGOUT_BUTTON}
    Wait Until Element Is Visible    ${LOGIN_FORM}
