class Homepage:

    # элементы домашней страницы
    yandex_page_title = "//head/meta[@content='Яндекс']"
    yandex_button_header = "//a[@class='Header_LogoYandex__3TSOI']/*"
    scooter_button_header = "//a[@class='Header_LogoScooter__3lsAR']/*"
    scooter_homepage = "//div[@class='Home_FirstPart__3g6vG']"
    # секция "Вопросы о важном"
    questions_section = "//div[@class='Home_FourPart__1uthg']"
    # кнопка "Заказать"
    order_button = "//div[contains(@class, 'Header')]/button[text()='Заказать']"
    # локаторы для вопроса "Сколько это стоит? И как оплатить?"
    question_price_collapsed = "//div[@aria-expanded='false'][text()='Сколько это стоит? И как оплатить?']"
    question_price_expanded = "//div[@aria-expanded='true'][text()='Сколько это стоит? И как оплатить?']"
    question_price_text = "//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"
    # локаторы для вопроса "Хочу сразу несколько самокатов! Так можно?"
    question_multiple_scooters_collapsed = "//div[@aria-expanded='false'][contains(.,'несколько самокатов!')]"
    question_multiple_scooters_expanded = "//div[@aria-expanded='true'][contains(.,'несколько самокатов!')]"
    question_multiple_scooters_text = "//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься" \
                                      " с друзьями, можете просто сделать несколько заказов — один за другим.']"
    # локаторы для вопроса "Как рассчитывается время аренды?"
    question_rental_time_collapsed = "//div[@aria-expanded='false'][contains(.,'время аренды?')]"
    question_rental_time_expanded = "//div[@aria-expanded='true'][contains(.,'время аренды?')]"
    question_rental_time_text = "//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в " \
                                "течение дня. Отсчёт времени аренды начинается с момента, " \
                                "когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, " \
                                "суточная аренда закончится 9 мая в 20:30.']"
    # локаторы для вопроса "Можно ли заказать самокат прямо на сегодня?"
    question_rent_scooter_today_collapsed = "//div[@aria-expanded='false'][contains(.,'заказать самокат прямо на сегодня?')]"
    question_rent_scooter_today_expanded = "//div[@aria-expanded='true'][contains(.,'заказать самокат прямо на сегодня?')]"
    question_rent_scooter_today_text = "//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']"
    # локаторы для вопроса "Можно ли продлить заказ или вернуть самокат раньше?"
    question_extend_rent_or_return_collapsed = "//div[@aria-expanded='false'][contains(.,'Можно ли продлить заказ')]"
    question_extend_rent_or_return_expanded = "//div[@aria-expanded='true'][contains(.,'Можно ли продлить заказ')]"
    question_extend_rent_or_return_text = "//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в " \
                                          "поддержку по красивому номеру 1010.']"
    # локаторы для вопроса "Вы привозите зарядку вместе с самокатом?"
    question_bring_charger_collapsed = "//div[@aria-expanded='false'][contains(.,'Вы привозите зарядку')]"
    question_bring_charger_expanded = "//div[@aria-expanded='true'][contains(.,'Вы привозите зарядку')]"
    question_bring_charger_text = "//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток" \
                                  " — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"
    # локаторы для вопроса "Можно ли отменить заказ?"
    question_cancel_order_collapsed = "//div[@aria-expanded='false'][contains(.,'Можно ли отменить заказ?')]"
    question_cancel_order_expanded = "//div[@aria-expanded='true'][contains(.,'Можно ли отменить заказ?')]"
    question_cancel_order_text = "//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки " \
                                 "тоже не попросим. Все же свои.']"
    # локаторы для вопроса "Я живу за МКАДом, привезёте?"
    question_live_in_suburb_collapsed = "//div[@aria-expanded='false'][contains(.,'Я жизу за МКАДом, привезёте?')]"
    question_live_in_suburb_expanded = "//div[@aria-expanded='true'][contains(.,'Я жизу за МКАДом, привезёте?')]"
    question_live_in_suburb_text = "//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']"


class OrderForm:

    # локаторы формы оформления заказа
    order_form = "//div[@class='Order_Form__17u6u']"
    about_order_form = "//div[@class='Order_Content__bmtHS']/*[text()='Про аренду']"
    name_field = "//input[@placeholder='* Имя']"
    surname_field = "//input[@placeholder='* Фамилия']"
    address_field = "//input[@placeholder='* Адрес: куда привезти заказ']"
    subway_field = "//input[@placeholder='* Станция метро']"
    station_name = "//*[text()='Черкизовская']"
    phone_field = "//input[@placeholder='* Телефон: на него позвонит курьер']"
    button_next = "//button[text()='Далее']"
    date_field = "//input[@placeholder='* Когда привезти самокат']"
    rent_time_field = "//div[text()='* Срок аренды']"
    rent_time_dropdown_option = "//div[text()='трое суток']"
    checkbox_black_color = "//input[@id='black']"
    checkbox_grey_color = "//input[@id='grey']"
    comment_field = "//input[@placeholder='Комментарий для курьера']"
    button_complete_order = "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"
    complete_order_popup = "//div[@class='Order_ModalHeader__3FDaJ']"
    button_complete_order_yes = "//button[text()='Да']"
    completed_order_popup = "//div[@class='Order_Text__2broi'][text()='Номер заказа: '][contains(.,'')]"
    completed_order_popup_text = "//div[@class='Order_Text__2broi']"
    details_order_number = "//div[@class='Track_Form__N4FE3']//input"
    button_see_order_status = "//button[text()='Посмотреть статус']"
