import pytest
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


@pytest.fixture()
def user_configure():
    user_methods = UserMethods()
    yield user_methods
    user_methods.logout_user()
    user_methods.delete_user()

@pytest.fixture()
def user(user_data, user_configure):
    user_configure.create_user(user_data)
    return user_configure

@pytest.fixture()
def user_with_login(user_data, user_configure):
    user_configure.create_user(user_data)
    user_configure.login_user(user_data)
    return user_configure, user_configure.headers

@pytest.fixture()
def order():
    return OrderMethods()
