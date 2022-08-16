import allure


@allure.title('Проверка вопроса "Сколько это стоит? И как оплатить?" в секции "Вопросы о важном".')
def test_question_how_much_does_it_costs(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Перейти к секции "Вопросы о важном"
    app.homepage_actions.scroll_to_questions()
    # Нажать на вопрос "Сколько это стоит? И как оплатить?"
    app.homepage_actions.click_question_how_much_does_it_costs()
    # Проверить, что текст под вопросом "Сколько это стоит? И как оплатить?" отобразился
    assert app.homepage_actions.answer_for_how_much_does_it_costs() == "Сутки — 400 рублей. Оплата курьеру — наличными" \
                                                                       " или картой.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Хочу сразу несколько самокатов! Так можно?" в секции "Вопросы о важном".')
def test_question_multiple_scooters_is_needed(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Перейти к секции "Вопросы о важном"
    app.homepage_actions.scroll_to_questions()
    # Нажать на вопрос "Хочу сразу несколько самокатов! Так можно?"
    app.homepage_actions.click_question_multiple_scooters_needed()
    # Проверить, что текст под вопросом "Хочу сразу несколько самокатов! Так можно?" отобразился
    assert app.homepage_actions.answer_for_multiple_scooters_needed() == "Пока что у нас так: один заказ — один " \
                                                                         "самокат. Если хотите покататься с друзьями, " \
                                                                         "можете просто сделать несколько заказов — " \
                                                                         "один за другим.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Как рассчитывается время аренды?" в секции "Вопросы о важном".')
def test_question_how_rental_time_is_calculated(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Перейти к секции "Вопросы о важном"
    app.homepage_actions.scroll_to_questions()
    # Нажать на вопрос "Как рассчитывается время аренды?"
    app.homepage_actions.click_question_how_rental_time_is_calculated()
    # Проверить, что текст под вопросом "Как рассчитывается время аренды?" отобразился
    assert app.homepage_actions.answer_for_how_rental_time_is_calculated() == "Допустим, вы оформляете заказ на 8 мая." \
                                                                              " Мы привозим самокат 8 мая в течение " \
                                                                              "дня. Отсчёт времени аренды начинается " \
                                                                              "с момента, когда вы оплатите заказ " \
                                                                              "курьеру. Если мы привезли самокат 8 мая" \
                                                                              " в 20:30, суточная аренда закончится " \
                                                                              "9 мая в 20:30.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Можно ли заказать самокат прямо на сегодня?" в секции "Вопросы о важном".')
def test_question_is_it_possible_to_rent_scooter_today(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Перейти к секции "Вопросы о важном"
    app.homepage_actions.scroll_to_questions()
    # Нажать на вопрос "Можно ли заказать самокат прямо на сегодня?"
    app.homepage_actions.click_question_is_it_possible_to_rent_scooter_today()
    # Проверить, что текст под вопросом "Можно ли заказать самокат прямо на сегодня?" отобразился
    assert app.homepage_actions.answer_for_is_it_possible_to_rent_scooter_today() == "Только начиная с завтрашнего дня." \
                                                                                     " Но скоро станем " \
                                                                                     "расторопнее.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Можно ли продлить заказ или вернуть самокат раньше?" в секции "Вопросы о важном".')
def test_question_extend_rent_or_return(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Перейти к секции "Вопросы о важном"
    app.homepage_actions.scroll_to_questions()
    # Нажать на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    app.homepage_actions.click_question_extend_rent_or_return()
    # Проверить, что текст под вопросом "Можно ли продлить заказ или вернуть самокат раньше?" отобразился
    assert app.homepage_actions.answer_for_extend_rent_or_return() == "Пока что нет! Но если что-то срочное — всегда " \
                                                                      "можно позвонить в поддержку по красивому " \
                                                                      "номеру 1010.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Вы привозите зарядку вместе с самокатом?" в секции "Вопросы о важном".')
def test_question_do_you_bring_charger(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Перейти к секции "Вопросы о важном"
    app.homepage_actions.scroll_to_questions()
    # Нажать на вопрос "Вы привозите зарядку вместе с самокатом?"
    app.homepage_actions.click_question_do_you_bring_charger()
    # Проверить, что текст под вопросом "Вы привозите зарядку вместе с самокатом?" отобразился
    assert app.homepage_actions.answer_for_do_you_bring_charger() == "Самокат приезжает к вам с полной зарядкой. Этого" \
                                                                     " хватает на восемь суток — даже если будете " \
                                                                     "кататься без передышек и во сне. Зарядка " \
                                                                     "не понадобится.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Можно ли отменить заказ?" в секции "Вопросы о важном".')
def test_question_can_cancel_order(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Перейти к секции "Вопросы о важном"
    app.homepage_actions.scroll_to_questions()
    # Нажать на вопрос "Можно ли отменить заказ?"
    app.homepage_actions.click_question_can_cancel_order()
    # Проверить, что текст под вопросом "Можно ли отменить заказ?" отобразился
    assert app.homepage_actions.answer_for_can_cancel_order() == "Да, пока самокат не привезли. Штрафа не будет, " \
                                                                 "объяснительной записки тоже не попросим. " \
                                                                 "Все же свои.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Я живу за МКАДом, привезёте?" в секции "Вопросы о важном".')
def test_question_live_in_suburb(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Перейти к секции "Вопросы о важном"
    app.homepage_actions.scroll_to_questions()
    # Нажать на вопрос "Я живу за МКАДом, привезёте?"
    app.homepage_actions.click_question_live_in_suburb()
    # Проверить, что текст под вопросом "Я живу за МКАДом, привезёте?" отобразился
    assert app.homepage_actions.answer_for_live_in_suburb() == "Да, обязательно. Всем самокатов! И Москве, и " \
                                                               "Московской области.", "Ответ на вопрос неверный!"
