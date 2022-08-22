import allure
from pages.homepage_actions import HomepageActions


@allure.title('Проверка вопроса "Сколько это стоит? И как оплатить?" в секции "Вопросы о важном".')
def test_question_how_much_does_it_costs(driver):
    homepage_actions = HomepageActions(driver)
    homepage_actions.scroll_to_questions()
    homepage_actions.click_question_how_much_does_it_costs()
    assert homepage_actions.answer_for_how_much_does_it_costs() == "Сутки — 400 рублей. Оплата курьеру — наличными или" \
                                                                   " картой.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Хочу сразу несколько самокатов! Так можно?" в секции "Вопросы о важном".')
def test_question_multiple_scooters_is_needed(driver):
    homepage_actions = HomepageActions(driver)
    homepage_actions.scroll_to_questions()
    homepage_actions.click_question_multiple_scooters_needed()
    assert homepage_actions.answer_for_multiple_scooters_needed() == "Пока что у нас так: один заказ — один самокат. " \
                                                                     "Если хотите покататься с друзьями, можете просто" \
                                                                     " сделать несколько заказов — один за другим.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Как рассчитывается время аренды?" в секции "Вопросы о важном".')
def test_question_how_rental_time_is_calculated(driver):
    homepage_actions = HomepageActions(driver)
    homepage_actions.scroll_to_questions()
    homepage_actions.click_question_how_rental_time_is_calculated()
    assert homepage_actions.answer_for_how_rental_time_is_calculated() == "Допустим, вы оформляете заказ на 8 мая. Мы" \
                                                                          " привозим самокат 8 мая в течение дня. " \
                                                                          "Отсчёт времени аренды начинается с момента," \
                                                                          " когда вы оплатите заказ курьеру. Если мы" \
                                                                          " привезли самокат 8 мая в 20:30, суточная" \
                                                                          " аренда закончится 9 мая в 20:30.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Можно ли заказать самокат прямо на сегодня?" в секции "Вопросы о важном".')
def test_question_is_it_possible_to_rent_scooter_today(driver):
    homepage_actions = HomepageActions(driver)
    homepage_actions.scroll_to_questions()
    homepage_actions.click_question_is_it_possible_to_rent_scooter_today()
    assert homepage_actions.answer_for_is_it_possible_to_rent_scooter_today() == "Только начиная с завтрашнего дня. Но" \
                                                                                 " скоро станем расторопнее.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Можно ли продлить заказ или вернуть самокат раньше?" в секции "Вопросы о важном".')
def test_question_extend_rent_or_return(driver):
    homepage_actions = HomepageActions(driver)
    homepage_actions.scroll_to_questions()
    homepage_actions.click_question_extend_rent_or_return()
    assert homepage_actions.answer_for_extend_rent_or_return() == "Пока что нет! Но если что-то срочное — всегда можно" \
                                                                  " позвонить в поддержку по красивому номеру 1010.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Вы привозите зарядку вместе с самокатом?" в секции "Вопросы о важном".')
def test_question_do_you_bring_charger(driver):
    homepage_actions = HomepageActions(driver)
    homepage_actions.scroll_to_questions()
    homepage_actions.click_question_do_you_bring_charger()
    assert homepage_actions.answer_for_do_you_bring_charger() == "Самокат приезжает к вам с полной зарядкой. Этого " \
                                                                 "хватает на восемь суток — даже если будете кататься" \
                                                                 " без передышек и во сне. Зарядка не понадобится.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Можно ли отменить заказ?" в секции "Вопросы о важном".')
def test_question_can_cancel_order(driver):
    homepage_actions = HomepageActions(driver)
    homepage_actions.scroll_to_questions()
    homepage_actions.click_question_can_cancel_order()
    assert homepage_actions.answer_for_can_cancel_order() == "Да, пока самокат не привезли. Штрафа не будет, " \
                                                             "объяснительной записки тоже не попросим. Все же свои.", "Ответ на вопрос неверный!"


@allure.title('Проверка вопроса "Я живу за МКАДом, привезёте?" в секции "Вопросы о важном".')
def test_question_live_in_suburb(driver):
    homepage_actions = HomepageActions(driver)
    homepage_actions.scroll_to_questions()
    homepage_actions.click_question_live_in_suburb()
    assert homepage_actions.answer_for_live_in_suburb() == "Да, обязательно. Всем самокатов! И Москве, и Московской " \
                                                           "области.", "Ответ на вопрос неверный!"
