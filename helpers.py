import allure
import json
import requests
import random
import string

from constant import URLS
from data import ORDERS
from http import HTTPStatus


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Генерация login, password и first_name курьера')
def generate_login_pass_first_name():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return login, password, first_name


@allure.step('Создаем курьера')
def register_new_courier(data=None):
    return requests.post(URLS.COURIER, data)


@allure.step('Создаем курьера и возвращаем список (login, password, first_name)')
def register_new_courier_and_return_login_password():
    login_pass = []
    login, password, first_name = generate_login_pass_first_name()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post((URLS.COURIER), data=payload)
    if response.status_code == HTTPStatus.CREATED:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


@allure.step('Авторизация курьера')
def login_courier(login_pass):
    payload = {
        "login": login_pass[0],
        "password": login_pass[1]
    }
    return requests.post(URLS.LOGIN_COURIER, data=payload)


@allure.step('Авторизация курьера и получение его "id"')
def login_existing_courier(login_pass):
    payload = {
        "login": login_pass[0],
        "password": login_pass[1]
    }
    response = requests.post((URLS.LOGIN_COURIER), data=payload)
    if response.status_code == HTTPStatus.OK:
        r = response.json()
        return r["id"]


@allure.step('Удаляем курьера')
def delete_courier(courier_id):
    return requests.delete(URLS.COURIER + str(courier_id))


@allure.step('Создаем заказ')
def create_order(data=None):
    return requests.post(URLS.ORDERS, data)


@allure.step('Получаем список заказов')
def get_list_of_orders():
    return requests.get(URLS.ORDERS)


@allure.step('Создаем заказ и получаем его "track"')
def create_order_return_track():
    payload_string = json.dumps(ORDERS.order_data)
    response = requests.post(URLS.ORDERS, data=payload_string)
    if response.status_code == HTTPStatus.CREATED:
        return response.json()["track"]


@allure.step('Получаем заказ по его "track"-номеру')
def get_order_by_track():
    track = create_order_return_track()
    return requests.get(f'{URLS.ORDER_GET}?t={track}')


@allure.step('Получаем "id" заказа по его "track"-номеру')
def get_order_id_by_track():
    track = create_order_return_track()
    response = requests.get(f'{URLS.ORDER_GET}?t={track}').json()
    return response["order"]["id"]


@allure.step('Принимаем заказ по id заказа и по id курьера')
def accept_order(order_id, payload):
    return requests.put(URLS.ORDER_ACCEPT + str(order_id), params=payload)

@allure.step('Завершить заказ')
def finish_order(order_id):
    return requests.put(URLS.ORDER_FINISH + str(order_id))
