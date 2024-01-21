import allure
import pytest
import pytest_check as check
import helpers

from constant import Errors
from http import HTTPStatus


class TestDeleteCourier:
    @allure.title('Проверка успешного удаления курьера')
    @allure.description('Проверяем, что успешный запрос возвращает правильный код ответа - 200 '
                        'и текст в ответе {"ok":true}')
    def test_delete_courier_success(self):
        login_pass = helpers.register_new_courier_and_return_login_password()
        courier_id = helpers.login_existing_courier(login_pass)
        response_raw = helpers.delete_courier(courier_id)
        response = response_raw.json()
        check.equal(response_raw.status_code, HTTPStatus.OK)
        check.is_in('ok', response)
        check.equal(response['ok'], True)


    @allure.title('Негативная проверка удаления курьера с несуществующим id')
    @allure.description('Проверяем, что отправка запроса с несуществующим id курьера возвращает ошибку с кодом ответа - 404'
                        'и текстом ответа "Курьера с таким id нет."')
    def test_negative_delete_courier_unexisting_id(self):
        response_raw = helpers.delete_courier(154895455)
        response = response_raw.json()
        check.equal(response_raw.status_code, HTTPStatus.NOT_FOUND)
        check.equal(response["message"], Errors.error_delete_no_such_id)
