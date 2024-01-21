import allure
import pytest
import pytest_check as check
from http import HTTPStatus

import helpers
from data import Login
from constant import Errors


class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    @allure.description('Проверяем, что запрос возвращает правильный код ответа - 201, успешный запрос возвращает'
                        ' {"ok":true}')
    def test_create_courier_success(self):
        login, password, first_name = helpers.generate_login_pass_first_name()
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response_raw = helpers.register_new_courier(data=data)
        response = response_raw.json()
        check.equal(response_raw.status_code, HTTPStatus.CREATED)
        check.is_in('ok', response)
        check.equal(response['ok'], True)
        login_pass = [login, password]
        courier_id = helpers.login_existing_courier(login_pass)
        helpers.delete_courier(courier_id)


    @allure.title('Проверка невозможности создания курьера с существующим логином (двух одинаковых курьеров)')
    @allure.description('Проверяем, что при попытке создать курьера с существующим логином, возвращается ошибка с кодом '
                        'ответа - 409 и текстом "Этот логин уже используется. Попробуйте другой."')
    def test_create_courier_existed_login(self):
        login, password, first_name = helpers.generate_login_pass_first_name()
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response_raw = helpers.register_new_courier(data=data)
        check.equal(response_raw.status_code, HTTPStatus.CREATED)
        response_raw_2 = helpers.register_new_courier(data=data)
        response_2 = response_raw_2.json()
        check.equal(response_raw_2.status_code, HTTPStatus.CONFLICT)
        check.equal(response_2['message'], Errors.error_login_already_exists)


    @allure.title('Параметризированная проверка невозможности создания курьера без заполнения обязательного поля ('
                  'login/password)')
    @allure.description('Проверяем, что при попытке создать курьера без заполнения обязательного поля, возвращается '
                        'ошибка с кодом ответа - 400 и текстом "Недостаточно данных для создания учетной записи."')
    @pytest.mark.parametrize('data', Login.data_create_without_required_field)
    def test_negative_create_courier_without_required_field(self, data):
        response_raw = helpers.register_new_courier(data=data)
        response = response_raw.json()
        check.equal(response_raw.status_code, HTTPStatus.BAD_REQUEST)
        check.equal(response['message'], Errors.error_create_no_data)
