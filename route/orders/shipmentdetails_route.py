"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import shipmentdetails_controller
from t08_flask_mysql.app.my_project.auth.dao import shipmentdetails_dao
from t08_flask_mysql.app.my_project.auth.domain import ShipmentDetails

shipmentdetails_bp = Blueprint('shipmentsdetails', __name__, url_prefix='/shipmentsdetails')


@shipmentdetails_bp.get('')
def get_all_products() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(shipmentdetails_controller.find_all()), HTTPStatus.OK)


@shipmentdetails_bp.post('')
def create_product() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    shipmentdetails = ShipmentDetails.create_from_dto(content)
    shipmentdetails_controller.create(shipmentdetails)
    return make_response(jsonify(shipmentdetails.put_into_dto()), HTTPStatus.CREATED)


@shipmentdetails_bp.get('/<int:shipmentdetails_id>')
def get_product(shipmentdetails_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(shipmentdetails_controller.find_by_id(shipmentdetails_id)), HTTPStatus.OK)


@shipmentdetails_bp.put('/<int:shipmentdetails_id>')
def update_product(shipmentdetails_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    shipmentdetails = ShipmentDetails.create_from_dto(content)
    shipmentdetails_controller.update(shipmentdetails_id, shipmentdetails)
    return make_response("ShipmentDetails updated", HTTPStatus.OK)


@shipmentdetails_bp.patch('/<int:shipmentdetails_id>')
def patch_product(shipmentdetails_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    shipmentdetails_controller.patch(shipmentdetails_id, content)
    return make_response("ShipmentDetails updated", HTTPStatus.OK)


@shipmentdetails_bp.delete('/<int:shipmentdetails_id>')
def delete_product(shipmentdetails_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    shipmentdetails_controller.delete(shipmentdetails_id)
    return make_response("ShipmentDetails deleted", HTTPStatus.OK)

@shipmentdetails_bp.get('/max-quantity')
def get_max_shipment_quantity() -> Response:
    max_quantity = shipmentdetails_dao.get_max_shipment_quantity()
    return make_response(jsonify({'max_quantity': max_quantity}), HTTPStatus.OK)