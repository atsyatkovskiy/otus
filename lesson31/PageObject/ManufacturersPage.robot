*** Settings ***
Library    SeleniumLibrary
Library    DatabaseLibrary
Resource    ../PageObject/BaseAdminPage.robot


*** Variables ***
${MANUFACTURERS_NAME_INPUT}    css=#input-name
${TABLE}    css=#form-category > div > table > tbody > tr
${VALUE}    Manufacturers_Name 0


*** Keywords ***
Open Menu Manufacturers
    Click Element    ${MENU_CATALOG}[0]
    ${catalog_items} =  Get Webelements  ${MENU_CATALOG_CHILD}[0]
    BuiltIn.Wait Until Keyword Succeeds  3 sec  1 sec  Click Element  ${catalog_items}[6]

Add Manufacturers
    [Arguments]    ${manufacturers_name}
    Click Element    ${ADD_BUTTON}[0]
    Input Text    ${MANUFACTURERS_NAME_INPUT}    ${manufacturers_name}
    Click Element    ${SAVE_BUTTON}[0]
