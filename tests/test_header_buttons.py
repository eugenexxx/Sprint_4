import allure


@allure.title('Проверка перехода на домашнюю страницу Яндекс по клику на кнопку в хедере.')
def test_click_yandex(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Нажимаем кнопку "Яндекс"
    app.header_actions.click_yandex_button()
    # Проверяем, что страница Яндекс открылась
    app.header_actions.wait_page_is_loaded()
    assert "https://yandex." in app.session.return_current_url(), "'Страница Яндекс не открылась!'"


@allure.title('Проверка перехода домашнюю страницу Яндекс.Самокат по клику на кнопку в хедере.')
def test_click_scooter(app):
    # Открываем страницу с формой заказа самоката
    app.session.open_page("/order")
    # Нажимаем кнопку "Самокат"
    app.header_actions.click_scooter_button()
    # Проверяем, что домашняя страница Яндекс.Самокат открылась
    app.header_actions.wait_yandex_scooter_homepage_is_displayed()
    assert "https://qa-scooter.praktikum-services.ru/" == app.driver.current_url, \
        "'Домашняя страница Яндекс.Самокат не открылась!'"

