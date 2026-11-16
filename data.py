from helpers import generate_courier_data


CREATE_USER_SUCCESS = '"success":true'
LOGIN_USER_SUCCESS = '"success":true'
PATCH_USER_SUCCESS = ("success", True)
CREATE_ORDER_SUCCESS = ("success", True)
GET_ORDERS_SUCCESS = ("success", True)

PATCH_USER_FAIL = ("success", False)
CREATE_ORDER_FAIL = ("success", False)
GET_ORDERS_FAIL = ("success", False)
USER_EXISTS_ERROR = 'User already exists'
NOT_ENOUGH_DATA_TO_CREATE = 'Email, password and name are required fields'
INVALID_USER_DATA = 'email or password are incorrect'

REQUIRED_USER_DATA = generate_courier_data()[0]
USER_DATA_WITHOUT_EMAIL = generate_courier_data()[1]
USER_DATA_WITHOUT_PASSWORD = generate_courier_data()[2]
USER_DATA_WITHOUT_NAME = generate_courier_data()[3]

(ALL_DATA, WITHOUT_EMAIL, WITHOUT_PASSWORD, WITHOUT_NAME, INVALID_EMAIL, INVALID_PASSWORD, NEW_EMAIL, NEW_PASSWORD,
 NEW_NAME) = generate_courier_data()

WITH_INGREDIENTS = {"ingredients":
                        ["6ae327a87e8698001b542b3b",
                         "6ae327a87e8698001b542b38",
                         "6ae327a87e8698001b542b45"
                         ]
                    }
INVALID_INGREDIENT = {"ingredients":
                          ["9999999999",
                           "6ae327a87e8698001b542b38",
                           "6ae327a87e8698001b542b45"
                           ]
                      }
NO_INGREDIENTS = {"ingredients":
                      []
                  }
