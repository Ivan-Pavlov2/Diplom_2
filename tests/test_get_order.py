import allure
import requests
from data.data import *


class TestGetOrders:
    @allure.title('Проверка на успешное получение заказов авторизованного пользователя')
    def test_get_orders_with_authorised_user(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[3]}
        create_order_number = requests.post(Links.order_url, headers=token, data=TestOrder.successful_order)
        get_order_number = requests.get(Links.order_url, headers=token)
        assert (get_order_number.status_code == 200
                and get_order_number.json()['orders'][0]['number'] == create_order_number.json()['order']['number'])

    @allure.title('Проверка на получение заказов пользователем без авторизации')
    def test_get_orders_without_authorisation(self, create_and_delete_user):
        response = requests.get(Links.order_url)
        assert response.status_code == 401 and response.json()['message'] == "You should be authorised"