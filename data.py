class LOGIN:
    data_existing_courier = {
        "login": "Maria98765",
        "password": "Qwerty123"
    }
    data_existing_courierId = 251795

    data_with_incorrect_required_field = [["Maria98765", "qwerty123"], ["maria98765", "Qwerty123"]]
    data_without_required_field = [["", "Qwerty123"], ["Maria159357", ""]]

    data_create_without_required_field = [
        {"login": "", "password": "Qwerty123"},   # отсутствует логин
        {"login": "Maria159357", "password": ""}  # отсутствует пароль
    ]

class ORDERS:

    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }
