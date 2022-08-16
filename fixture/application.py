from selenium import webdriver
import allure
from fixture.session import SessionHelper
from actions.homepage_actions import HomepageActions
from actions.order_scooter_form_actions import OrderScooterFormActions
from actions.header_check_actions import HeaderActions


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.homepage_actions = HomepageActions(self)
        self.order_scooter = OrderScooterFormActions(self)
        self.header_actions = HeaderActions(self)

    @allure.step('Закрыть страницу.')
    def destroy(self):
        self.driver.quit()
