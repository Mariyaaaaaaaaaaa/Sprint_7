import json

import allure
import pytest
import pytest_check as check
import requests

import helpers
from constant import URLS
from data import ORDERS
from http import HTTPStatus


@allure.title('Параметризированная проверка - при создании заказа возможно выбрать один из цветов самоката ('
              'черный/серый), выбрать оба цвета, не выбрать ни одного цвета (необязательное поле {color})')
@allure.description('Проверяем, что при создании заказа можно указать один из цветов, можно указать оба цвета, '
                    'можно совсем не указывать цвет. В ответ возвращается  код 201, и тело ответа содержит "track"')
@pytest.mark.parametrize('color',
                         [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
def test_create_order_color(color):
    """ Параметризированная проверка - при создании заказа возможно выбрать один из цветов самоката (черный/серый),
        выбрать оба цвета, не выбрать ни одного цвета (необязательное поле {color}) """

    order_data = ORDERS.order_data
    order_data["color"] = color
    response_raw = helpers.create_order(data=json.dumps(order_data))
    response = response_raw.json()
    check.equal(response_raw.status_code, HTTPStatus.CREATED)
    check.is_in('track', response)
    track = response['track']
    r = requests.get(f'{URLS.ORDER_GET}?t={track}').json()
    order_id = r["order"]["id"]
    helpers.finish_order(order_id)

@allure.title('Проверка получения списка заказов')
@allure.description('Проверяем, что при запросе списка заказов в ответе возвращается код 200, в ответе есть поле '
                    '"orders", тип поля "orders" - список')
def test_get_list_of_orders():
    response_raw = helpers.get_list_of_orders()
    response = response_raw.json()

    print(response_raw.status_code)
    assert HTTPStatus.OK == response_raw.status_code
    assert 'orders' in response
    assert type(response['orders']) == list
