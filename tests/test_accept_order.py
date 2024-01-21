import allure

import helpers
from data import LOGIN
from http import HTTPStatus


@allure.title('Проверка успешного принятия заказа')
@allure.description('Принимаем заказ по id заказа - {order_id} и id курьера - {courierId}. Успешный запрос возвращает '
                    'правильный код ответа - 200 и текст в ответе {"ok":true}')
def test_accept_order_success():
    order_id = helpers.get_order_id_by_track()
    payload = {'courierId': LOGIN.data_existing_courierId}
    response_raw = helpers.accept_order(order_id, payload)
    response = response_raw.json()
    assert HTTPStatus.OK == response_raw.status_code
    assert response == {"ok": True}
    helpers.finish_order(order_id)

