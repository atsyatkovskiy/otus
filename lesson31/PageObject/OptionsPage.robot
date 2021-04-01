*** Settings ***
Library    SeleniumLibrary
Library    DatabaseLibrary
Resource    ../PageObject/BaseAdminPage.robot


*** Variables ***
${OPTION_NAME_INPUT}    css=input[name="option_description[1][name]"]
${TYPE_SELECT_INPUT}    css=select[name="type"]
${SORT_ORDER_INPUT}    css=#input-sort-order
${TABLE}    css=#form-category > div > table > tbody > tr
${VALUE}    Option_Name_date 123


*** Keywords ***
Open Menu Options
    Click Element    ${MENU_CATALOG}[0]
    ${catalog_items} =  Get Webelements  ${MENU_CATALOG_CHILD}[0]
    BuiltIn.Wait Until Keyword Succeeds  3 sec  1 sec  Click Element  ${catalog_items}[5]

Add options
    [Arguments]    ${options_name}    ${date}    ${sort_order}
    Click Element    ${ADD_BUTTON}[0]
    Input Text    ${OPTION_NAME_INPUT}    ${options_name}
    Select From List By Value    ${TYPE_SELECT_INPUT}    ${date}
    Input Text    ${SORT_ORDER_INPUT}    ${sort_order}
    Click Element    ${SAVE_BUTTON}[0]
