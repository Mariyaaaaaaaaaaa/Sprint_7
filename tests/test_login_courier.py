import allure
import pytest
import pytest_check as check

from http import HTTPStatus

import helpers
from data import LOGIN
from constant import ERRORS


@allure.title('Проверка успешной авторизации курьера')
@allure.description('Проверяем, что запрос возвращает правильный код ответа - 200, успешный запрос возвращает'
                    ' в ответе "id"')
def test_login_courier_success():
    login_pass = helpers.register_new_courier_and_return_login_password()
    response_raw = helpers.login_courier(login_pass)
    response = response_raw.json()
    assert HTTPStatus.OK == response_raw.status_code
    assert 'id' in response
    courier_id = helpers.login_existing_courier(login_pass)
    helpers.delete_courier(courier_id)
    


@allure.title('Параметризированная проверка невозможности авторизации курьера, если неправильно указано одно из '
              'обязательных полей (login/password)')
@allure.description('Проверяем, что при попытке авторизации курьера с некорректно указанным одним из обязательных '
                    'полей возвращается ошибка с кодом ответа 404, и текстом "Учетная запись не найдена"')
@pytest.mark.parametrize('data', LOGIN.data_with_incorrect_required_field)
def test_negative_login_with_incorrect_required_field(data):
    response_raw = helpers.login_courier(data)
    response = response_raw.json()
    check.equal(response_raw.status_code, HTTPStatus.NOT_FOUND)
    check.equal(response['message'], ERRORS.error_login_not_found)


@allure.title('Параметризированная проверка невозможности авторизации курьера, если отсутствует одно из обязательных '
              'полей (login/password)')
@allure.description('Проверяем, что при попытке авторизации курьера с неуказанным/пустым обязательным полем'
                    'login/password возвращается ошибка с кодом ответа 400, и текстом "Недостаточно данных для входа"')
@pytest.mark.parametrize('data', LOGIN.data_without_required_field)
def test_negative_login_without_required_field(data):
    response_raw = helpers.login_courier(data)
    response = response_raw.json()
    check.equal(response_raw.status_code, HTTPStatus.BAD_REQUEST)
    check.equal(response['message'], ERRORS.error_login_no_data)


@allure.title('Проверка невозможности авторизации курьера под несуществующим пользователем')
@allure.description('Проверяем, что при попытке авторизации несуществуего курьера'
                    'возвращается ошибка с кодом ответа 404, и текстом "Учетная запись не найдена"')
def test_login_with_nonexistent_courier():
    login_pass = []
    login, password, first_name = helpers.generate_login_pass_first_name()  # Cоздаем логин и пароль, но не регистрируем курьера
    login_pass.append(login)
    login_pass.append(password)
    response_raw = helpers.login_courier(login_pass)
    response = response_raw.json()
    check.equal(response_raw.status_code, 404)
    check.equal(response['message'], ERRORS.error_login_not_found)
