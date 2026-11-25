from helpers import generate_user_data


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

REQUIRED_USER_DATA = generate_user_data()[0]
USER_DATA_WITHOUT_EMAIL = generate_user_data()[1]
USER_DATA_WITHOUT_PASSWORD = generate_user_data()[2]
USER_DATA_WITHOUT_NAME = generate_user_data()[3]

(ALL_DATA, WITHOUT_EMAIL, WITHOUT_PASSWORD, WITHOUT_NAME, INVALID_EMAIL, INVALID_PASSWORD, NEW_EMAIL, NEW_PASSWORD,
 NEW_NAME) = generate_user_data()

WITH_INGREDIENTS = {"ingredients":
                        ["691577430cc94f001a65b859",
                         "691577430cc94f001a65b866",
                         "691577430cc94f001a65b85c"
                         ]
                    }
INVALID_INGREDIENT = {"ingredients":
                          ["9999999999",
                           "691577430cc94f001a65b866",
                           "691577430cc94f001a65b85c"
                           ]
                      }
NO_INGREDIENTS = {"ingredients":
                      []
                  }
