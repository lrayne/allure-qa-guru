import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature('Управление реестром')
    allure.dynamic.story('Создание реестра')
    allure.dynamic.link('https://github.com', name='Github')
    allure.dynamic.title('Название тест-кейса')
    pass


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.feature('Управление реестром')
@allure.story('Создание реестра')
@allure.link('https://github.com', name='Github')
@allure.title('Название тест-кейса')
def test_decorator_lables():
    pass
