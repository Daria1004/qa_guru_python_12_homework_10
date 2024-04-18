import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_decorator_labels():
    open_page()
    search_repository('eroshenkoam/allure-example')
    open_repository('eroshenkoam/allure-example')
    open_issues_tab()
    should_be_number('#76')


@allure.step('Открываем главную страницу')
def open_page():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo}')
def search_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo)
    s('#query-builder-test').submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def open_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issues_tab():
    s('#issues-tab').click()


@allure.step('Проверяем наличие Issue с номером {number}')
def should_be_number(number):
    s(by.partial_text(number)).should(be.visible)
