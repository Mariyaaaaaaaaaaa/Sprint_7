class URLS:
    SERVER_URL = 'http://qa-scooter.praktikum-services.ru/'
    COURIER = SERVER_URL + 'api/v1/courier/'
    LOGIN_COURIER = COURIER + 'login'
    ORDERS = SERVER_URL + 'api/v1/orders'
    ORDER_ACCEPT = ORDERS + '/accept/'
    ORDER_GET = ORDERS + '/track'
    ORDER_FINISH = ORDERS + '/finish/'



class ERRORS:
    error_login_no_data = "Недостаточно данных для входа"
    error_login_not_found = "Учетная запись не найдена"

    error_create_no_data = "Недостаточно данных для создания учетной записи"
    error_login_already_exists = "Этот логин уже используется. Попробуйте другой."

    error_delete_no_data = "Недостаточно данных для удаления курьера"
    error_delete_no_such_id = "Курьера с таким id нет."

    error_count_orders_no_data = "Недостаточно данных для поиска"
    error_count_orders_courier_not_found = "Курьер не найден"

    error_track_order_no_data = "Недостаточно данных для поиска"
    error_track_order_order_not_found = "Заказ не найден"

    error_accept_order_no_order_number = "Недостаточно данных для поиска"
    error_accept_order_no_such_courier = "Курьера с таким id не существует"
    error_accept_order_no_data = "Недостаточно данных для поиска"
