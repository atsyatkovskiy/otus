*** Settings ***
Library    String

Resource  ../PageObject/UserPage.robot
Resource  ../Resources/DataBase.robot

Suite Setup    Connect To Database    pymysql    ${DBName}    ${DBUser}    ${DBPass}    ${DBHost}    ${DBPort}
Suite Teardown  Disconnect From Database

Test Setup    Open Browser    url=NONE    options=${OPTIONS}    browser=${BROWSER}    remote_url=http://${REMOTE_EXECUTOR}:4444/wd/hub
#Test Setup    Open Browser    url=NONE    options=${OPTIONS}    browser=${BROWSER}
Test Teardown    Close Browser


*** Variables ***
${BROWSER}    chrome
${REMOTE_EXECUTOR}    localhost
${OPTIONS}    add_argument("--ignore-certificate-errors");add_argument("--start-maximized")
${DBName}    bitnami_opencart
${DBUser}    bn_opencart
${DBPass}
${DBHost}    127.0.0.1
${DBPort}    3306
${URL}    http://192.168.1.34/

@{DATA} =    Name    Last_name    test@mail.test    +12345678    qwerty


*** Test Cases ***
Add New User
    [Teardown]    Run Keywords    Execute Sql String    delete from ${CUSTOMER_DB} where firstname = '${DATA}[0]' and lastname = '${DATA}[1]'
    ...  AND  Close Browser
    Go To    ${URL}
    UserPage.Go To Register Form
    UserPage.Register New User    ${DATA}
    Wait Until Keyword Succeeds    3 sec    1 sec    Check User In Database    ${DATA}
