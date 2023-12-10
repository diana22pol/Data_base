"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import webaddress_controller
from t08_flask_mysql.app.my_project.auth.domain import Webaddress

webaddress_bp = Blueprint('webaddresses', __name__, url_prefix='/webaddresses')


@webaddress_bp.get('')
def get_all_webaddresses() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(webaddress_controller.find_all()), HTTPStatus.OK)


@webaddress_bp.post('')
def create_webaddress() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    webaddress = Webaddress.create_from_dto(content)
    webaddress_controller.create(webaddress)
    return make_response(jsonify(webaddress.put_into_dto()), HTTPStatus.CREATED)


@webaddress_bp.get('/<int:webaddress_id>')
def get_webaddress(webaddress_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(webaddress_controller.find_by_id(webaddress_id)), HTTPStatus.OK)


@webaddress_bp.put('/<int:webaddress_id>')
def update_webaddress(webaddress_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    country = Webaddress.create_from_dto(content)
    webaddress_controller.update(webaddress_id, country)
    return make_response("Webaddress updated", HTTPStatus.OK)


@webaddress_bp.patch('/<int:webaddress_id>')
def patch_webaddress(webaddress_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    webaddress_controller.patch(webaddress_id, content)
    return make_response("Webaddress updated", HTTPStatus.OK)


@webaddress_bp.delete('/<int:webaddress_id>')
def delete_webaddressr(webaddress_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    webaddress_controller.delete(webaddress_id)
    return make_response("Webaddress deleted", HTTPStatus.OK)
