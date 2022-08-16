import allure


class SessionHelper:

    def __init__(self, app):
        self.app = app

    @allure.step('Открыть страницу.')
    def open_page(self, link):
        driver = self.app.driver
        driver.maximize_window()
        driver.get("https://qa-scooter.praktikum-services.ru" + link)
        driver.implicitly_wait(60)

    @allure.step("Вернуть адрес страницы.")
    def return_current_url(self):
        driver = self.app.driver
        return driver.current_url

