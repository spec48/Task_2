import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_courier_data():
    email = f'{generate_random_string(5)}@ya.ru'
    password = generate_random_string(5)
    name = generate_random_string(5)
    all_fields = {
        "email": email,
        "password": password,
        "name": name
    }
    without_email = {
        "password": password,
        "name": name
    }
    without_password = {
        "email": email,
        "name": name
    }
    without_name = {
        "email": email,
        "password": password,
    }
    invalid_email = {
        "email": "1111111@ya.ru",
        "password": password
    }
    invalid_password = {
        "email": email,
        "password": "99999999"
    }
    new_email = {
        "email": "newemail@ya.ru",
        "password": password,
        "name": name
    }
    new_password = {
        "email": email,
        "password": "newpassword",
        "name": name
    }
    new_name = {
        "email": email,
        "password": password,
        "name": "newname"
    }
    return (all_fields,
            without_email,
            without_password,
            without_name,
            invalid_email,
            invalid_password,
            new_email,
            new_password,
            new_name)
