from pages.header_check_actions import HeaderActions
import allure


@allure.title('Проверка перехода на домашнюю страницу Яндекс по клику на кнопку в хедере.')
def test_click_yandex(driver):
    header_actions = HeaderActions(driver)
    header_actions.click_yandex_button()
    header_actions.wait_page_is_loaded()
    assert "https://yandex." in driver.current_url, "'Страница Яндекс не открылась!'"


@allure.title('Проверка перехода домашнюю страницу Яндекс.Самокат по клику на кнопку в хедере.')
def test_click_scooter(driver):
    link = driver.current_url + "order"
    driver.get(url=link)
    header_actions = HeaderActions(driver)
    header_actions.click_scooter_button()
    header_actions.wait_yandex_scooter_homepage_is_displayed()
    assert "https://qa-scooter.praktikum-services.ru/" == driver.current_url, "'Домашняя страница Яндекс.Самокат не открылась!'"

