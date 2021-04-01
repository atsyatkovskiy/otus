*** Settings ***
Library    SeleniumLibrary
Resource    ../PageObject/BaseAdminPage.robot
Resource    ../PageObject/CategoriesPage.robot
Resource    ../PageObject/OptionsPage.robot
Resource    ../PageObject/ManufacturersPage.robot

Documentation    Tests OpentCart with Robot Framework

Suite Setup    Open Browser    url=NONE    options=${OPTIONS}    browser=${BROWSER}    remote_url=http://${REMOTE_EXECUTOR}:4444/wd/hub
#Suite Setup    Open Browser    url=NONE    options=${OPTIONS}    browser=${BROWSER}
Suite Teardown    Close Browser


*** Variables ***
# C переменными работать через опцию -v
${BROWSER}    chrome
${REMOTE_EXECUTOR}    localhost
${OPTIONS}    add_argument("--ignore-certificate-errors");add_argument("--start-maximized")


*** Test Cases ***
Test login and logout admin page
    [Tags]  Login/Logout
    BaseAdminPage.Login admin user
    BaseAdminPage.Logout Admin User

Test add categories
    [Tags]  Add_categories
    BaseAdminPage.Login admin user
    CategoriesPage.Open Menu Categories
    CategoriesPage.Add Categories    Apple_category_name    Apple_tag_title
    CategoriesPage.Item Table

Test add options
    [Tags]  Add_options
    BaseAdminPage.Login admin user
    OptionsPage.Open Menu Options
    OptionsPage.Add Options    Option_Name_date    date    123

Test add manufacturers
    [Tags]  Add_manufacturers
    BaseAdminPage.Login admin user
    ManufacturersPage.Open Menu Manufacturers
    ManufacturersPage.Add Manufacturers    Manufacturers_Name
