from typing import List
from my_project.auth.domain.orders import Order
from my_project.auth.dao.general_dao import GeneralDAO


class OrderDAO(GeneralDAO):
    _domain_type = Order

    def update(self, order: Order):
        """
        Оновлює замовлення в базі даних.
        :param order: об'єкт замовлення з оновленими даними
        """
        self._session.merge(order)
        self._session.commit()

    def delete(self, order_id: int):
        """
        Видаляє замовлення з бази даних за його ID.
        :param order_id: ідентифікатор замовлення
        """
        order = self._session.query(Order).get(order_id)
        if order:
            self._session.delete(order)
            self._session.commit()
