class Links:
    register_url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    user_url = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    login_url = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    order_url = 'https://stellarburgers.nomoreparties.site/api/orders'


class UserWithoutRequiredFields:
    no_name = {"email": "pavlov_ivan2124@yandex.ru", "password": "123456"}
    no_email = {"password": "123456", "name": "Ivan"}
    no_password = {"email": "pavlov_ivan2124@yandex.ru", "name": "Ivan"}
    empty_name = {"name": "", "email": "pavlov_ivan2124@yandex.ru", "password": "123456"}
    empty_email = {"email": "", "password": "123456", "name": "Sanya"}
    empty_password = {"email": "pavlov_ivan2124@yandex.ru", "password": "", "name": "Ivan"}


class TestOrder:
    successful_order = {
  "ingredients": [
    "61c0c5a71d1f82001bdaaa6e",
    "61c0c5a71d1f82001bdaaa76",
    "61c0c5a71d1f82001bdaaa7a",
    "61c0c5a71d1f82001bdaaa74",
    "61c0c5a71d1f82001bdaaa6c"
  ]
}
    bad_order = {"ingredients":  ["bad_ingredient"]}