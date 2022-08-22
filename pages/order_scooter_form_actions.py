from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OrderForm
import allure
import datetime
import time


class OrderScooterFormActions:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждём пока форма заказа отобразится.')
    def wait_order_form_is_displayed(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, OrderForm.order_form)))

    @allure.step('Заполнить поле "Имя".')
    def fill_field_name(self, name):
        self.driver.find_element("xpath", OrderForm.name_field).send_keys(name)

    @allure.step('Заполнить поле "Фамилия".')
    def fill_field_surname(self, surname):
        self.driver.find_element("xpath", OrderForm.surname_field).send_keys(surname)

    @allure.step('Заполнить поле "Адрес".')
    def fill_field_address(self, address):
        self.driver.find_element("xpath", OrderForm.address_field).send_keys(address)

    @allure.step('Заполнить поле "Метро".')
    def fill_field_subway(self):
        self.driver.find_element("xpath", OrderForm.subway_field).click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, OrderForm.station_name)))
        self.driver.find_element("xpath", OrderForm.station_name).click()

    @allure.step('Заполнить поле "Телефон".')
    def fill_field_phone(self, phone):
        self.driver.find_element("xpath", OrderForm.phone_field).send_keys(phone)

    @allure.step('Заполнить поля секции "Для кого самокат".')
    def fill_for_whom_section(self, name, surname, address, phone):
        self.fill_field_name(name)
        self.fill_field_surname(surname)
        self.fill_field_address(address)
        self.fill_field_subway()
        self.fill_field_phone(phone)

    @allure.step('Нажать кнопку "Далее".')
    def click_button_next(self):
        self.driver.find_element("xpath", OrderForm.button_next).click()

    @allure.step('Ждём пока форма "Про аренду" отобразится.')
    def wait_about_order_form_is_displayed(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, OrderForm.about_order_form)))

    @allure.step('Заполнить поле "Дата".')
    def fill_field_date(self):
        next_day = datetime.datetime.today() + datetime.timedelta(days=1)
        next_day_formatted = next_day.strftime('%d.%m.%Y')
        self.driver.find_element("xpath", OrderForm.date_field).send_keys(next_day_formatted)

    @allure.step('Заполнить поле "Срок аренды".')
    def fill_field_rent_time(self):
        self.driver.find_element("xpath", OrderForm.rent_time_field).click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, OrderForm.rent_time_dropdown_option)))
        self.driver.find_element("xpath", OrderForm.rent_time_dropdown_option).click()

    @allure.step('Нажать кнопку "Чёрный жемчуг" в списке "Цвет самоката".')
    def click_black_color_checkbox(self):
        self.driver.find_element("xpath", OrderForm.checkbox_black_color).click()

    @allure.step('Нажать кнопку "Серая безысходность" в списке "Цвет самоката".')
    def click_grey_color_checkbox(self):
        self.driver.find_element("xpath", OrderForm.checkbox_grey_color).click()

    @allure.step('Заполнить поле "Комментарий для курьера".')
    def fill_field_comment(self, comment):
        self.driver.find_element("xpath", OrderForm.comment_field).send_keys(comment)

    @allure.step('Заполнить поля секции "Для кого самокат".')
    def fill_about_order_section(self, comment):
        self.fill_field_rent_time()
        self.fill_field_date()
        self.click_black_color_checkbox()
        self.click_grey_color_checkbox()
        self.fill_field_comment(comment)

    @allure.step('Нажать кнопку "Заказать".')
    def click_button_complete_order(self):
        self.driver.find_element("xpath", OrderForm.button_complete_order).click()

    @allure.step('Ждём пока всплывающее окно "Хотите оформить заказ?" отобразится.')
    def wait_complete_order_popup_is_displayed(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, OrderForm.complete_order_popup)))

    @allure.step('Нажать кнопку "Да" в окне "Хотите оформить заказ?".')
    def click_button_yes(self):
        self.driver.find_element("xpath", OrderForm.button_complete_order_yes).click()

    @allure.step('Ждём пока всплывающее окно "Заказ оформлен" отобразится.')
    def wait_order_success_popup_is_displayed(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, OrderForm.completed_order_popup)))
        pop_text = self.driver.find_element("xpath", OrderForm.completed_order_popup_text).text
        if len(pop_text) < 68:
            time.sleep(5)
        else:
            pass

    @allure.step('Нажать кнопку "Посмотреть статус" в окне "Заказ оформлен".')
    def click_button_see_order_status(self):
        self.driver.find_element("xpath", OrderForm.button_see_order_status).click()

    @allure.step('Возвращаем имя заказчика.')
    def customer_name(self, name):
        customer_name = f"//div[@class='Track_OrderInfo__2fpDL']//*[text()='{name}']"
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, customer_name)))
        return self.driver.find_element("xpath", customer_name).text
