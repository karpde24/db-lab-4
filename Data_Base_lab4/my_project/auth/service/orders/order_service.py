from my_project.auth.dao.orders.order_dao import OrderDAO
from my_project.auth.domain.orders import Order


class OrderService:
    def __init__(self, dao: OrderDAO):
        self._dao = dao

    def update(self, order: Order):
        """
        Оновлює замовлення в базі даних.
        :param order: об'єкт замовлення з оновленими даними
        """
        self._dao.update(order)

    def delete(self, order_id: int):
        """
        Видаляє замовлення з бази даних за його ID.
        :param order_id: ідентифікатор замовлення
        """
        self._dao.delete(order_id)
