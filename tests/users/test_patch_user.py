import allure
import pytest
from data import ALL_DATA, NEW_EMAIL, PATCH_USER_SUCCESS, NEW_NAME, NEW_PASSWORD, PATCH_USER_FAIL


class TestPatchUser:

    @allure.title('Успешное обновление поля email пользователя')
    @allure.description('Тест проверяет код и тело ответа при успешном обновлении поля email пользователя')
    @pytest.mark.parametrize("user_data, new_data", [
        [ALL_DATA, NEW_EMAIL]
    ]
                             )
    def test_patch_user_patch_email_status_code_200(self, user_with_login, user_data, new_data):
        status_code, response_body = user_with_login[0].patch_user(new_data)
        assert (status_code == 200 and PATCH_USER_SUCCESS in response_body.items() and
                response_body.get('user').get('email') == NEW_EMAIL.get('email')), \
            f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Успешное обновление поля name пользователя')
    @allure.description('Тест проверяет код и тело ответа при успешном обновлении поля name пользователя')
    @pytest.mark.parametrize("user_data, new_data", [
        [ALL_DATA, NEW_NAME]
    ]
                             )
    def test_patch_user_patch_name_status_code_200(self, user_with_login, user_data, new_data):
        status_code, response_body = user_with_login[0].patch_user(new_data)
        assert (status_code == 200 and PATCH_USER_SUCCESS in response_body.items() and
                response_body.get('user').get('name') == NEW_NAME.get('name')), \
            f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Успешное обновление поля password пользователя')
    @allure.description('Тест проверяет код и тело ответа при успешном обновлении поля password пользователя')
    @pytest.mark.parametrize("user_data, new_data", [
        [ALL_DATA, NEW_PASSWORD]
    ]
                             )
    def test_patch_user_patch_password_status_code_200(self, user_with_login, user_data, new_data):
        status_code, response_body = user_with_login[0].patch_user(new_data)
        assert status_code == 200 and PATCH_USER_SUCCESS in response_body.items(), \
            f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Невозможно обновить поля email, password, name у неавторизованного пользователя')
    @allure.description('Тест проверяет код ошибки и тело ответа при обновлении полей email, password, name '
                        'у неавторизованного пользователя')
    @pytest.mark.parametrize("user_data, new_data", [
        [ALL_DATA, NEW_EMAIL],
        [ALL_DATA, NEW_PASSWORD],
        [ALL_DATA, NEW_NAME]
    ]
                             )
    def test_patch_user_user_without_login_patch_email_password_name_status_code_401(self, user, user_data, new_data):
        status_code, response_body = user.patch_user(new_data)
        assert status_code == 401 and PATCH_USER_FAIL in response_body.items(), \
            f'Код ответа: {status_code}, тело ответа: {response_body}'
