import allure
import pytest_check as check
from http import HTTPStatus

import helpers


@allure.title('Проверка получения заказа по его номеру')
@allure.description('Получаем заказ по его "track" - номеру. Успешный запрос возвращает '
                    'правильный код ответа - 200 и наличие поля "order" в ответе')
def test_get_order_by_track():
    response_raw = helpers.get_order_by_track()
    response = response_raw.json()
    check.equal(HTTPStatus.OK, response_raw.status_code)
    check.is_in("order", response)
    order_id = helpers.get_order_id_by_track
    helpers.finish_order(order_id)
