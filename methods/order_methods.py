import allure
import requests
from urls import BASE_URL, ORDERS_URL


class OrderMethods:

    def __init__(self):
        self.url = f'{BASE_URL}{ORDERS_URL}'

    @allure.step("Создать заказ")
    def create_order(self, params, token):
        response = requests.post(self.url, headers=token,
                                 json=params)
        try:
            return response.status_code, response.json()
        except requests.exceptions.JSONDecodeError:
            return response.status_code, response.text

    @allure.step("Получить заказы")
    def get_orders(self, token):
        response = requests.get(self.url, headers=token)
        return response.status_code, response.json()
