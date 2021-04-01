*** Settings ***
Library    SeleniumLibrary
Library    DatabaseLibrary
Resource    ../PageObject/BaseAdminPage.robot


*** Variables ***
${NAME_INPUT}    css=#input-name1
${TAG_TITLE_INPUT}    css=#input-meta-title1
${TABLE}    css=#form-category > div > table > tbody > tr
${VALUE}    Apple_category_name 0


*** Keywords ***
Open menu categories
    Click Element    ${MENU_CATALOG}[0]
    ${catalog_items} =  Get Webelements  ${MENU_CATALOG_CHILD}[0]
    BuiltIn.Wait Until Keyword Succeeds  3 sec  1 sec  Click Element  ${catalog_items}[0]

Add categories
    [Arguments]    ${category_name}    ${tag_title}
    Click Element    ${ADD_BUTTON}[0]
    Input Text    ${NAME_INPUT}    ${category_name}
    Input Text    ${TAG_TITLE_INPUT}    ${tag_title}
    Click Element    ${SAVE_BUTTON}[0]

Item table
    ${test_item}=    Get Text    ${TABLE}
    ${count_element}=    Get Element Count    ${TABLE}
    Log To Console    ${test_item}
    Log To Console    Это количество элементов - ${count_element}
