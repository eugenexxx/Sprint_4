from locators import Homepage
import logging
import allure

LOGGER = logging.getLogger(__name__)


class HomepageActions:

    def __init__(self, app):
        self.app = app

    @allure.step('Нажать кнопку "Заказать".')
    def click_order_button(self):
        LOGGER.info('Нажать кнопку "Заказать".')
        self.app.driver.find_element("xpath", Homepage.order_button).click()

    @allure.step('Перейти к секции "Вопросы о важном".')
    def scroll_to_questions(self):
        LOGGER.info('Перейти к секции "Вопросы о важном"')
        questions_section = self.app.driver.find_element("xpath", Homepage.questions_section)
        self.app.driver.execute_script("arguments[0].scrollIntoView();", questions_section)

    @allure.step('Нажать на вопрос "Сколько это стоит? И как оплатить?".')
    def click_question_how_much_does_it_costs(self):
        self.app.driver.find_element("xpath", Homepage.question_price_collapsed).is_enabled()
        LOGGER.info('Нажать на вопрос "Сколько это стоит? И как оплатить?".')
        self.app.driver.find_element("xpath", Homepage.question_price_collapsed).click()

    @allure.step('Проверить, что ответ на вопрос "Сколько это стоит? И как оплатить?" отобразился.')
    def answer_for_how_much_does_it_costs(self):
        self.app.driver.find_element("xpath", Homepage.question_price_expanded).is_enabled()
        LOGGER.info('Проверить, что ответ на вопрос "Сколько это стоит? И как оплатить?" отобразился.')
        return self.app.driver.find_element("xpath", Homepage.question_price_text).text

    @allure.step('Нажать на вопрос "Хочу сразу несколько самокатов! Так можно?".')
    def click_question_multiple_scooters_needed(self):
        self.app.driver.find_element("xpath", Homepage.question_multiple_scooters_collapsed).is_enabled()
        LOGGER.info('Нажать на вопрос "Хочу сразу несколько самокатов! Так можно?".')
        self.app.driver.find_element("xpath", Homepage.question_multiple_scooters_collapsed).click()

    @allure.step('Проверить, что ответ на вопрос "Хочу сразу несколько самокатов! Так можно?" отобразился.')
    def answer_for_multiple_scooters_needed(self):
        self.app.driver.find_element("xpath", Homepage.question_multiple_scooters_expanded).is_enabled()
        LOGGER.info('Проверить, что ответ на вопрос "Хочу сразу несколько самокатов! Так можно?" отобразился.')
        return self.app.driver.find_element("xpath", Homepage.question_multiple_scooters_text).text

    @allure.step('Нажать на вопрос "Как рассчитывается время аренды?".')
    def click_question_how_rental_time_is_calculated(self):
        self.app.driver.find_element("xpath", Homepage.question_rental_time_collapsed).is_enabled()
        LOGGER.info('Нажать на вопрос "Как рассчитывается время аренды?".')
        self.app.driver.find_element("xpath", Homepage.question_rental_time_collapsed).click()

    @allure.step('Проверить, что ответ на вопрос "Как рассчитывается время аренды?" отобразился.')
    def answer_for_how_rental_time_is_calculated(self):
        self.app.driver.find_element("xpath", Homepage.question_rental_time_expanded).is_enabled()
        LOGGER.info('Проверить, что ответ на вопрос "Как рассчитывается время аренды?" отобразился.')
        return self.app.driver.find_element("xpath", Homepage.question_rental_time_text).text

    @allure.step('Нажать на вопрос "Можно ли заказать самокат прямо на сегодня?".')
    def click_question_is_it_possible_to_rent_scooter_today(self):
        self.app.driver.find_element("xpath", Homepage.question_rent_scooter_today_collapsed).is_enabled()
        LOGGER.info('Нажать на вопрос "Можно ли заказать самокат прямо на сегодня?".')
        self.app.driver.find_element("xpath", Homepage.question_rent_scooter_today_collapsed).click()

    @allure.step('Проверить, что ответ на вопрос "Можно ли заказать самокат прямо на сегодня?" отобразился.')
    def answer_for_is_it_possible_to_rent_scooter_today(self):
        self.app.driver.find_element("xpath", Homepage.question_rent_scooter_today_expanded).is_enabled()
        LOGGER.info('Проверить, что ответ на вопрос "Можно ли заказать самокат прямо на сегодня?" отобразился.')
        return self.app.driver.find_element("xpath", Homepage.question_rent_scooter_today_text).text

    @allure.step('Нажать на вопрос "Можно ли продлить заказ или вернуть самокат раньше?".')
    def click_question_extend_rent_or_return(self):
        self.app.driver.find_element("xpath", Homepage.question_extend_rent_or_return_collapsed).is_enabled()
        LOGGER.info('Нажать на вопрос "Можно ли продлить заказ или вернуть самокат раньше?".')
        self.app.driver.find_element("xpath", Homepage.question_extend_rent_or_return_collapsed).click()

    @allure.step('Проверить, что ответ на вопрос "Можно ли продлить заказ или вернуть самокат раньше?" отобразился.')
    def answer_for_extend_rent_or_return(self):
        self.app.driver.find_element("xpath", Homepage.question_extend_rent_or_return_expanded).is_enabled()
        LOGGER.info('Проверить, что ответ на вопрос "Можно ли продлить заказ или вернуть самокат раньше?" отобразился.')
        return self.app.driver.find_element("xpath", Homepage.question_extend_rent_or_return_text).text

    @allure.step('Нажать на вопрос "Вы привозите зарядку вместе с самокатом?".')
    def click_question_do_you_bring_charger(self):
        self.app.driver.find_element("xpath", Homepage.question_bring_charger_collapsed).is_enabled()
        LOGGER.info('Нажать на вопрос "Вы привозите зарядку вместе с самокатом?".')
        self.app.driver.find_element("xpath", Homepage.question_bring_charger_collapsed).click()

    @allure.step('Проверить, что ответ на вопрос "Вы привозите зарядку вместе с самокатом?" отобразился.')
    def answer_for_do_you_bring_charger(self):
        self.app.driver.find_element("xpath", Homepage.question_bring_charger_expanded).is_enabled()
        LOGGER.info('Проверить, что ответ на вопрос "Вы привозите зарядку вместе с самокатом?" отобразился.')
        return self.app.driver.find_element("xpath", Homepage.question_bring_charger_text).text

    @allure.step('Нажать на вопрос "Можно ли отменить заказ?".')
    def click_question_can_cancel_order(self):
        self.app.driver.find_element("xpath", Homepage.question_cancel_order_collapsed).is_enabled()
        LOGGER.info('Нажать на вопрос "Можно ли отменить заказ?".')
        self.app.driver.find_element("xpath", Homepage.question_cancel_order_collapsed).click()

    @allure.step('Проверить, что ответ на вопрос "Можно ли отменить заказ?" отобразился.')
    def answer_for_can_cancel_order(self):
        self.app.driver.find_element("xpath", Homepage.question_cancel_order_expanded).is_enabled()
        LOGGER.info('Проверить, что ответ на вопрос "Можно ли отменить заказ?" отобразился.')
        return self.app.driver.find_element("xpath", Homepage.question_cancel_order_text).text

    @allure.step('Нажать на вопрос "Я живу за МКАДом, привезёте?".')
    def click_question_live_in_suburb(self):
        self.app.driver.find_element("xpath", Homepage.question_live_in_suburb_collapsed).is_enabled()
        LOGGER.info('Нажать на вопрос "Я живу за МКАДом, привезёте?".')
        self.app.driver.find_element("xpath", Homepage.question_live_in_suburb_collapsed).click()

    @allure.step('Проверить, что ответ на вопрос "Я живу за МКАДом, привезёте?" отобразился.')
    def answer_for_live_in_suburb(self):
        self.app.driver.find_element("xpath", Homepage.question_live_in_suburb_expanded).is_enabled()
        LOGGER.info('Проверить, что ответ на вопрос "Я живу за МКАДом, привезёте?" отобразился.')
        return self.app.driver.find_element("xpath", Homepage.question_live_in_suburb_text).text
