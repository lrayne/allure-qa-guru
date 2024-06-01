import allure
from selene import browser, by, be


def test_search_issue():

    with allure.step('Открыть \'github.com\''):
        browser.open('https://github.com')

    with allure.step(
        'Ввести в поисковое поле \'eroshenkoam/allure-example\' и нажать \'Enter\''
    ):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type(
            'eroshenkoam/allure-example'
        ).press_enter()

    with allure.step('В \'results\' нажать на \'eroshenkoam/allure-example\''):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Нажать на \'Issues\''):
        browser.element('#issues-tab').click()

    with allure.step('Issue с номером #89 отображается на странице'):
        browser.element(by.partial_text("#89")).should(be.visible)
