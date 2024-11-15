class OrderController:
    # Інші методи контролера

    def update(self, order_id: int, order: Order):
        """
        Оновлює існуюче замовлення за його ID.
        :param order_id: ідентифікатор замовлення
        :param order: новий об'єкт замовлення
        """
        existing_order = self.find_by_id(order_id)
        if existing_order:
            existing_order.pick_up_location = order.pick_up_location
            existing_order.drop_off_location = order.drop_off_location
            # Оновлення інших полів за необхідності
            self._service.update(existing_order)

    def delete(self, order_id: int):
        """
        Видаляє замовлення за його ID.
        :param order_id: ідентифікатор замовлення
        """
        self._service.delete(order_id)
