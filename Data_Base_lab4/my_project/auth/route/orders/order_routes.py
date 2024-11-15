from flask import Blueprint, jsonify, Response, request, make_response
from http import HTTPStatus

from my_project.auth.controller.orders import order_controller
from my_project.auth.domain.orders import Order

order_bp = Blueprint('orders', __name__, url_prefix='/orders')


@order_bp.get('/<int:order_id>')
def get_order(order_id: int) -> Response:
    """
    Отримує замовлення за його ID.
    :param order_id: ідентифікатор замовлення
    :return: Response object
    """
    return make_response(jsonify(order_controller.find_by_id(order_id)), HTTPStatus.OK)


@order_bp.post('')
def create_order() -> Response:
    """
    Створює нове замовлення.
    :return: Response object
    """
    content = request.get_json()
    order = Order(**content)
    order_controller.create(order)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.CREATED)


@order_bp.put('/<int:order_id>')
def update_order(order_id: int) -> Response:
    """
    Оновлює замовлення за його ID.
    :param order_id: ідентифікатор замовлення
    :return: Response object
    """
    content = request.get_json()
    order = Order(**content)
    order_controller.update(order_id, order)
    return make_response("Order updated", HTTPStatus.OK)


@order_bp.delete('/<int:order_id>')
def delete_order(order_id: int) -> Response:
    """
    Видаляє замовлення за його ID.
    :param order_id: ідентифікатор замовлення
    :return: Response object
    """
    order_controller.delete(order_id)
    return make_response("Order deleted", HTTPStatus.OK)
