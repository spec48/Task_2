import allure
import requests
from urls import BASE_URL, USER_URL


class UserMethods:

    def __init__(self):
        self.headers = None
        self.dict_token = None
        self.url = f'{BASE_URL}{USER_URL}'
        self._logged_in = False

    @allure.step("Создать пользователя")
    def create_user(self, user_data):
        response = requests.post(f'{self.url}register', data=user_data)
        bearer_token = response.json().get("accessToken")
        if self.headers is None:
            self.headers = {'Authorization': f'{bearer_token}'}
        return response.status_code, response.text

    @allure.step("Удалить пользователя")
    def delete_user(self):
        if self.headers == {'Authorization': 'None'}:
            return None
        response = requests.delete(f'{self.url}user', headers=self.headers)
        return response.status_code, response.text

    @allure.step("Login пользователя")
    def login_user(self, user_data):
        response = requests.post(f'{self.url}login', data=user_data)
        refresh_token = response.json().get("refreshToken")
        self._logged_in = True
        if self.dict_token is None:
            self.dict_token = {'token': f'{refresh_token}'}
        return response.status_code, response.text

    @allure.step("Logout пользователя")
    def logout_user(self):
        if self.dict_token == {'token': 'None'} or self.dict_token is None:
            return None
        response = requests.post(f'{self.url}logout', data=self.dict_token)
        self._logged_in = False
        return response.status_code, response.text

    @allure.step("Обновить данные пользователя")
    def patch_user(self, user_new_data):
        if self._logged_in:
            response = requests.patch(f'{self.url}user', headers=self.headers, data=user_new_data)
            return response.status_code, response.json()
        else:
            response = requests.patch(f'{self.url}user', headers=None, data=user_new_data)
            return response.status_code, response.json()
