import allure
import pytest
from data import WITH_INGREDIENTS, REQUIRED_USER_DATA, CREATE_ORDER_SUCCESS, NO_INGREDIENTS, CREATE_ORDER_FAIL, \
    INVALID_INGREDIENT


class TestCreateOrder:

    @allure.title('Успешное создание заказа с ингредиентами авторизованным пользователем')
    @allure.description('Тест проверяет код и тело ответа при создании заказа с ингредиентами '
                        'авторизованным пользователем')
    @pytest.mark.parametrize("user_data, ingredients", [
        [REQUIRED_USER_DATA, WITH_INGREDIENTS]
    ]
                             )
    def test_create_order_with_ingredients_logged_in_user_status_code_200(self, user_with_login, order,
                                                                          user_data, ingredients):
        status_code, response_body = order.create_order(ingredients, user_with_login[1])
        assert status_code == 200 and CREATE_ORDER_SUCCESS in response_body.items(), \
            f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Успешное создание заказа с ингредиентами неавторизованным пользователем')
    @allure.description('Тест проверяет код и тело ответа при создании заказа с ингредиентами '
                        'неавторизованным пользователем')
    @pytest.mark.parametrize("user_data, ingredients", [
        [REQUIRED_USER_DATA, WITH_INGREDIENTS]
    ]
                             )
    def test_create_order_with_ingredients_user_without_login_status_code_200(self, user, order,
                                                                          user_data, ingredients):
        status_code, response_body = order.create_order(ingredients, None)
        assert status_code == 200 and CREATE_ORDER_SUCCESS in response_body.items(), \
            f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Невозможно создать заказ без ингредиентов авторизованным пользователем')
    @allure.description('Тест проверяет код ошибки и тело ответа при создании заказа без ингредиентов '
                        'авторизованным пользователем')
    @pytest.mark.parametrize("user_data, ingredients", [
        [REQUIRED_USER_DATA, NO_INGREDIENTS]
    ]
                             )
    def test_create_order_without_ingredients_logged_in_user_status_code_400(self, user_with_login, order,
                                                                              user_data, ingredients):
        status_code, response_body = order.create_order(ingredients, user_with_login[1])
        assert status_code == 400 and CREATE_ORDER_FAIL in response_body.items(), \
            f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Невозможно создать заказ без ингредиентов неавторизованным пользователем')
    @allure.description('Тест проверяет код ошибки и тело ответа при создании заказа без ингредиентов '
                        'неавторизованным пользователем')
    @pytest.mark.parametrize("user_data, ingredients", [
        [REQUIRED_USER_DATA, NO_INGREDIENTS]
    ]
                             )
    def test_create_order_without_ingredients_without_login_status_code_400(self, user, order,
                                                                             user_data, ingredients):
        status_code, response_body = order.create_order(ingredients, None)
        assert status_code == 400 and CREATE_ORDER_FAIL in response_body.items(), \
            f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Невозможно создать заказ c несуществующим хешем ингредиента авторизованным пользователем')
    @allure.description('Тест проверяет код ошибки и тело ответа при создании заказа c несуществующим хешем ингредиента '
                        'авторизованным пользователем')
    @pytest.mark.parametrize("user_data, ingredients", [
        [REQUIRED_USER_DATA, INVALID_INGREDIENT]
    ]
                             )
    def test_create_order_with_invalid_ingredient_logged_in_user_status_code_500(self, user_with_login, order,
                                                              user_data, ingredients):
        status_code, response_body = order.create_order(ingredients, user_with_login[1])
        assert status_code == 500, f'Код ответа: {status_code}, тело ответа: {response_body}'


    @allure.title('Невозможно создать заказ c несуществующим хешем ингредиента неавторизованным пользователем')
    @allure.description('Тест проверяет код ошибки и тело ответа при создании заказа c несуществующим хешем ингредиента '
                        'неавторизованным пользователем')
    @pytest.mark.parametrize("user_data, ingredients", [
        [REQUIRED_USER_DATA, INVALID_INGREDIENT]
    ]
                             )
    def test_create_order_with_invalid_ingredient_without_login_status_code_500(self, user, order,
                                                                                user_data, ingredients):
        status_code, response_body = order.create_order(ingredients, None)
        assert status_code == 500, f'Код ответа: {status_code}, тело ответа: {response_body}'
