import allure
import pytest_check as check

from http import HTTPStatus

import helpers
from data import Login


class TestAcceptOrder:
    @allure.title('Проверка успешного принятия заказа')
    @allure.description('Принимаем заказ по id заказа - {order_id} и id курьера - {courierId}. Успешный запрос '
                        'возвращает правильный код ответа - 200 и текст в ответе {"ok":true}')
    def test_accept_order_success(self):
        order_id = helpers.get_order_id_by_track()
        payload = {'courierId': Login.data_existing_courierId}
        response_raw = helpers.accept_order(order_id, payload)
        response = response_raw.json()
        check.equal(response_raw.status_code, HTTPStatus.OK)
        check.equal(response, {"ok": True})
        helpers.finish_order(order_id)
