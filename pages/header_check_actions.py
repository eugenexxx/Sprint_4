from locators import Homepage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class HeaderActions:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать кнопку "Яндекс" в хедере.')
    def click_yandex_button(self):
        self.driver.find_element("xpath", Homepage.yandex_button_header).click()

    @allure.step('Ждем пока страница откроется.')
    def wait_page_is_loaded(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, Homepage.yandex_page_title)))

    @allure.step('Нажать кнопку "Самокат" в хедере.')
    def click_scooter_button(self):
        self.driver.find_element("xpath", Homepage.scooter_button_header).click()

    @allure.step('Ждём пока домашняя страница Яндекс.Самокат откроется.')
    def wait_yandex_scooter_homepage_is_displayed(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, Homepage.scooter_homepage)))
