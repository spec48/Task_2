import allure
import pytest
from data import REQUIRED_USER_DATA, CREATE_USER_SUCCESS, USER_EXISTS_ERROR, USER_DATA_WITHOUT_EMAIL, \
    USER_DATA_WITHOUT_PASSWORD, USER_DATA_WITHOUT_NAME, NOT_ENOUGH_DATA_TO_CREATE


class TestCreateUser:

    @allure.title('Успешное создание уникального пользователя с обязательными полями')
    @allure.description('Тест проверяет код и тело ответа при создании пользователя с обязательными полями')
    @pytest.mark.parametrize("user_data", [REQUIRED_USER_DATA])
    def test_create_user_with_email_password_and_name_status_code_200(self, user_configure, user_data):
        status_code, response_body = user_configure.create_user(user_data)
        assert status_code == 200 and CREATE_USER_SUCCESS in response_body, \
            f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Невозможно создание двух одинаковых пользователей')
    @allure.description('Тест проверяет код ошибки и тело ответа при создании пользователя, который уже существует')
    @pytest.mark.parametrize("user_data", [REQUIRED_USER_DATA])
    def test_create_user_two_identical_users_status_code_403(self, user, user_data):
        status_code_create_error, response_body_create_error = user.create_user(user_data)
        assert status_code_create_error == 403 and USER_EXISTS_ERROR in response_body_create_error, \
            f'Код ответа: {status_code_create_error}, тело ответа: {response_body_create_error}'


    @allure.title('Невозможно создание пользователя с одним незаполненным обязательным полем')
    @allure.description('Тест проверяет код ошибки и тело ответа при создании пользователя с одним незаполненным полем')
    @pytest.mark.parametrize("user_data", [USER_DATA_WITHOUT_EMAIL,
                                           USER_DATA_WITHOUT_PASSWORD,
                                           USER_DATA_WITHOUT_NAME
                                           ]
                             )
    def test_create_user_without_one_required_field_status_code_403(self, user_configure, user_data):
        status_code_create_error, response_body_create_error = user_configure.create_user(user_data)
        assert status_code_create_error == 403 and NOT_ENOUGH_DATA_TO_CREATE in response_body_create_error, \
            f'Код ответа: {status_code_create_error}, тело ответа: {response_body_create_error}'
