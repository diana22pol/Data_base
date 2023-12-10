"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import sale_controller
from t08_flask_mysql.app.my_project.auth.domain import Sale

sale_bp = Blueprint('sales', __name__, url_prefix='/sales')


@sale_bp.get('')
def get_all_sales() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(sale_controller.find_all()), HTTPStatus.OK)


@sale_bp.post('')
def create_sale() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    sale = Sale.create_from_dto(content)
    sale_controller.create(sale)
    return make_response(jsonify(sale.put_into_dto()), HTTPStatus.CREATED)


@sale_bp.get('/<int:sale_id>')
def get_sale(sale_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(sale_controller.find_by_id(sale_id)), HTTPStatus.OK)


@sale_bp.put('/<int:sale_id>')
def update_sale(sale_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    sale = Sale.create_from_dto(content)
    sale_controller.update(sale_id, sale)
    return make_response("Sale updated", HTTPStatus.OK)


@sale_bp.patch('/<int:sale_id>')
def patch_sale(sale_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    sale_controller.patch(sale_id, content)
    return make_response("Sale updated", HTTPStatus.OK)


@sale_bp.delete('/<int:sale_id>')
def delete_sale(sale_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    sale_controller.delete(sale_id)
    return make_response("Sale deleted", HTTPStatus.OK)


@sale_bp.get('/<int:sale_id>/sale-details')
def get_sales_details(sale_id: int) -> Response:
    """
    Gets stores where the employee works.
    :param sale_id: ID of the employee
    :return: Response object with stores where the employee works
    """
    sale = Sale.query.get(sale_id)
    return make_response(jsonify(sale.get_sales_details()), HTTPStatus.OK)
