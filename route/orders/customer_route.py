"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import customer_controller
from t08_flask_mysql.app.my_project.auth.domain import Customer

customer_bp = Blueprint('customers', __name__, url_prefix='/customers')


@customer_bp.get('')
def get_all_customers() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(customer_controller.find_all()), HTTPStatus.OK)


@customer_bp.post('')
def create_customer() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    customer = Customer.create_from_dto(content)
    customer_controller.create(customer)
    return make_response(jsonify(customer.put_into_dto()), HTTPStatus.CREATED)


@customer_bp.get('/<int:customer_id>')
def get_customer(customer_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(customer_controller.find_by_id(customer_id)), HTTPStatus.OK)


@customer_bp.put('/<int:customer_id>')
def update_customer(customer_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    customer = Customer.create_from_dto(content)
    customer_controller.update(customer_id, customer)
    return make_response("Customer updated", HTTPStatus.OK)


@customer_bp.patch('/<int:customer_id>')
def patch_country(customer_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    customer_controller.patch(customer_id, content)
    return make_response("Customer updated", HTTPStatus.OK)


@customer_bp.delete('/<int:customer_id>')
def delete_customer(customer_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    customer_controller.delete(customer_id)
    return make_response("Customer deleted", HTTPStatus.OK)

@customer_bp.get('/<int:customer_id>/sales')
def get_customer_sales(customer_id: int) -> Response:
    """
    Gets stores where the employee works.
    :param customer_id: ID of the employee
    :return: Response object with stores where the employee works
    """
    customer = Customer.query.get(customer_id)
    return make_response(jsonify(customer.get_customer_sales()), HTTPStatus.OK)
