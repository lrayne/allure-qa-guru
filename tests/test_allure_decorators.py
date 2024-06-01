import allure
from selene import browser, by, be


def test_search_issue():
    open_site('https://github.com')

    search_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    click_issues_tab()

    issue_should_be_visible('#89')


@allure.step('Открыть {link}')
def open_site(link):
    browser.open(link)


@allure.step('Ввести в поисковое поле {value} и нажать \'Enter\'')
def search_repository(value):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type(value).press_enter()


@allure.step('В \'results\' нажать на ссылку {link}')
def go_to_repository(link):
    browser.element(by.link_text(link)).click()


@allure.step('Нажать на "Issues"')
def click_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Issue {number} отображается на странице')
def issue_should_be_visible(number):
    browser.element(by.partial_text(number)).should(be.visible)
