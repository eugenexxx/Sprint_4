from locators import Homepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import allure

LOGGER = logging.getLogger(__name__)


class HeaderActions:

    def __init__(self, app):
        self.app = app

    @allure.step('Нажать кнопку "Яндекс" в хедере.')
    def click_yandex_button(self):
        LOGGER.info('Нажать кнопку "Яндекс" в хедере.')
        self.app.driver.find_element("xpath", Homepage.yandex_button_header).click()

    @allure.step('Проверить, что страница открылась.')
    def wait_page_is_loaded(self):
        LOGGER.info('Проверить, что страница открылась.')
        self.app.driver.switch_to.window(self.app.driver.window_handles[1])
        try:
            wait = WebDriverWait(self.app.driver, 20)
            wait.until(EC.presence_of_element_located((By.XPATH, Homepage.yandex_page_title)))
        except AssertionError:
            LOGGER.info('Страница Яндекс не открылась!')

    @allure.step('Нажать кнопку "Самокат" в хедере.')
    def click_scooter_button(self):
        LOGGER.info('Нажать кнопку "Самокат" в хедере.')
        self.app.driver.find_element("xpath", Homepage.scooter_button_header).click()

    @allure.step('Проверить, что домашняя страница Яндекс.Самокат открылась.')
    def wait_yandex_scooter_homepage_is_displayed(self):
        LOGGER.info('Проверить, что домашняя страница Яндекс.Самокат открылась.')
        try:
            wait = WebDriverWait(self.app.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, Homepage.scooter_homepage)))
        except AssertionError:
            LOGGER.info('Страница Яндекс.Самокат не открылась!')
