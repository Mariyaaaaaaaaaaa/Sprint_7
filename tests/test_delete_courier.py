import allure
import pytest

import helpers

from constant import ERRORS
from http import HTTPStatus


@allure.title('Проверка успешного удаления курьера')
@allure.description('Проверяем, что успешный запрос возвращает правильный код ответа - 200 '
                    'и текст в ответе {"ok":true}')
def test_delete_courier_success():
    login_pass = helpers.register_new_courier_and_return_login_password()
    id = helpers.login_existing_courier(login_pass)
    response_raw = helpers.delete_courier(id)
    response = response_raw.json()
    assert HTTPStatus.OK == response_raw.status_code
    assert 'ok' in response
    assert response['ok'] == True
    assert response == {'ok': True}


@allure.title('Негативная проверка удаления курьера с несуществующим id')
@allure.description('Проверяем, что отправка запроса с несуществующим id курьера возвращает ошибку с кодом ответа - 404'
                    'и текстом ответа "Курьера с таким id нет."')
def test_negative_delete_courier_unexisting_id():
    response_raw = helpers.delete_courier(154895455)
    response = response_raw.json()
    assert HTTPStatus.NOT_FOUND == response_raw.status_code
    assert response["message"] == ERRORS.error_delete_no_such_id

