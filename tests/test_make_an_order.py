import allure


@allure.title('Проверка формы заказа самоката.')
def test_make_new_order(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Нажимаем кнопку "Заказать"
    app.homepage_actions.click_order_button()
    # Проверяем, что форма заказа отобразилась
    app.order_scooter.check_order_form_is_displayed()
    # Заполняем форму "Для кого самокат"
    app.order_scooter.fill_for_whom_section(
        name="Иван",
        surname="Иванов",
        address="ул. Пушкина, д. Колотушкина",
        phone="12345678901")
    # Нажимаем кнопку "Далее"
    app.order_scooter.click_button_next()
    # Проверяем, что форма "Про аренду" отобразилась
    app.order_scooter.check_about_order_form_is_displayed()
    # Заполняем форму "Для кого самокат"
    app.order_scooter.fill_about_order_section(comment="Авто-тест")
    # Нажимаем кнопку "Заказать"
    app.order_scooter.click_button_complete_order()
    # Проверяем, что всплывающее окно "Хотите оформить заказ?" отобразилась
    app.order_scooter.check_complete_order_popup_is_displayed()
    # Нажимаем кнопку "Да" в окне "Хотите оформить заказ?"
    app.order_scooter.click_button_yes()
    # Проверяем, что всплывающее окно "Заказ оформлен" отобразилась
    app.order_scooter.order_success_popup_is_displayed()
    # Нажимаем кнопку "Посмотреть статус" в окне "Хотите оформить заказ?"
    app.order_scooter.click_button_see_order_status()
    # Нажимаем кнопку "Посмотреть статус" в окне "Хотите оформить заказ?"
    assert app.order_scooter.customer_name(name="Иван") == "Иван", \
        "Имя заказчика не совпадает с именем показанным на экране!"
