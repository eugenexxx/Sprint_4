from pages.homepage_actions import HomepageActions
from pages.order_scooter_form_actions import OrderScooterFormActions
import allure


@allure.title('Проверка формы заказа самоката.')
def test_make_new_order(driver):
    homepage_actions = HomepageActions(driver)
    order_scooter = OrderScooterFormActions(driver)
    homepage_actions.click_order_button()
    order_scooter.wait_order_form_is_displayed()
    order_scooter.fill_for_whom_section(
        name="Иван",
        surname="Иванов",
        address="ул. Пушкина, д. Колотушкина",
        phone="12345678901")
    order_scooter.click_button_next()
    order_scooter.wait_about_order_form_is_displayed()
    order_scooter.fill_about_order_section(comment="Авто-тест")
    order_scooter.click_button_complete_order()
    order_scooter.wait_complete_order_popup_is_displayed()
    order_scooter.click_button_yes()
    order_scooter.wait_order_success_popup_is_displayed()
    order_scooter.click_button_see_order_status()
    assert order_scooter.customer_name(name="Иван") == "Иван", "Имя заказчика не совпадает с именем показанным на экране!"
