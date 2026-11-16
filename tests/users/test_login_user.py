import allure
import pytest
from data import REQUIRED_USER_DATA, LOGIN_USER_SUCCESS, ALL_DATA, WITHOUT_NAME, INVALID_EMAIL, \
    INVALID_USER_DATA, INVALID_PASSWORD, USER_DATA_WITHOUT_NAME


class TestLoginUser:

    @allure.title('Успешный логин пользователя при заполнении всех полей')
    @allure.description('Тест проверяет код и тело ответа при успешном логине пользователя и заполнении всех полей')
    @pytest.mark.parametrize("user_data", [REQUIRED_USER_DATA])
    def test_login_user_valid_data_user_status_code_200(self, user, user_data):
        status_code, response_body = user.login_user(user_data)
        assert status_code == 200 and LOGIN_USER_SUCCESS in response_body, \
            f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Успешный логин пользователя при заполнении полей email, password')
    @allure.description('Тест проверяет код и тело ответа при успешном логине пользователя '
                        'и заполнении полей email, password')
    @pytest.mark.parametrize("user_data, user_data_without_name", [[ALL_DATA, WITHOUT_NAME]])
    def test_login_user_data_user_without_name_status_code_200(self, user, user_data, user_data_without_name):
        status_code, response_body = user.login_user(user_data_without_name)
        assert status_code == 200 and LOGIN_USER_SUCCESS in response_body, \
            f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Невозможен логин пользователя с неверными полями email и password')
    @allure.description('Тест проверяет код ошибки и тело ответа при логине пользователя с неверными email и password')
    @pytest.mark.parametrize("user_data, invalid_email_password", [[ALL_DATA, USER_DATA_WITHOUT_NAME]])
    def test_login_user_invalid_email_and_password_status_code_401(self, user, user_data, invalid_email_password):
        status_code, response_body = user.login_user(invalid_email_password)
        assert status_code == 401 and INVALID_USER_DATA in response_body, \
            f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Невозможен логин пользователя с неверным полем email')
    @allure.description('Тест проверяет код ошибки и тело ответа при логине пользователя с неверным полем email')
    @pytest.mark.parametrize("user_data, user_data_invalid_email", [[ALL_DATA, INVALID_EMAIL]])
    def test_login_user_invalid_email_status_code_401(self, user, user_data, user_data_invalid_email):
        status_code, response_body = user.login_user(user_data_invalid_email)
        assert status_code == 401 and INVALID_USER_DATA in response_body, \
            f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Невозможен логин пользователя с неверным полем password')
    @allure.description('Тест проверяет код ошибки и тело ответа при логине пользователя с неверным полем password')
    @pytest.mark.parametrize("user_data, user_data_invalid_password", [[ALL_DATA, INVALID_PASSWORD]])
    def test_login_user_invalid_password_status_code_401(self, user, user_data, user_data_invalid_password):
        status_code, response_body = user.login_user(user_data_invalid_password)
        assert status_code == 401 and INVALID_USER_DATA in response_body, \
            f'Код ответа: {status_code}, тело ответа: {response_body}'
