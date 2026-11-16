import allure
import pytest
from data import GET_ORDERS_SUCCESS, ALL_DATA, WITH_INGREDIENTS, GET_ORDERS_FAIL


class TestGetOrders:

    @allure.title('Успешное получение заказов авторизованным пользователем')
    @allure.description('Тест проверяет код и тело ответа при получении заказов авторизованным пользователем')
    @pytest.mark.parametrize("user_data, ingredients", [
        [ALL_DATA, WITH_INGREDIENTS]
    ]
                             )
    def test_get_orders_logged_in_user_status_code_200(self, order, user_with_login, user_data, ingredients):
        order.create_order(ingredients, user_with_login[1])
        status_code, response_body = order.get_orders(user_with_login[1])
        assert (status_code == 200 and GET_ORDERS_SUCCESS in response_body.items() and
                isinstance(response_body.get('orders')[0].get('number'), int),
                f'Код ответа: {status_code}, тело ответа: {response_body}')


    @allure.title('Невозможно получение заказов неавторизованным пользователем')
    @allure.description('Тест проверяет код ошибки и тело ответа при получении заказов неавторизованным пользователем')
    @pytest.mark.parametrize("user_data, ingredients", [
        [ALL_DATA, WITH_INGREDIENTS]
    ]
                             )
    def test_get_orders_without_login_status_code_401(self, order, user_with_login, user_data, ingredients):
        order.create_order(ingredients, user_with_login[1])
        status_code, response_body = order.get_orders(None)
        assert (status_code == 401 and GET_ORDERS_FAIL in response_body.items(),
                f'Код ответа: {status_code}, тело ответа: {response_body}')
