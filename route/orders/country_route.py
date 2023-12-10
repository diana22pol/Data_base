"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import country_controller
from t08_flask_mysql.app.my_project.auth.domain import Country

country_bp = Blueprint('countries', __name__, url_prefix='/countries')


@country_bp.get('')
def get_all_countries() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(country_controller.find_all()), HTTPStatus.OK)


@country_bp.post('')
def create_country() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    country = Country.create_from_dto(content)
    country_controller.create(country)
    return make_response(jsonify(country.put_into_dto()), HTTPStatus.CREATED)


@country_bp.get('/<int:country_id>')
def get_country(country_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(country_controller.find_by_id(country_id)), HTTPStatus.OK)


@country_bp.put('/<int:country_id>')
def update_country(country_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    country = Country.create_from_dto(content)
    country_controller.update(country_id, country)
    return make_response("Country updated", HTTPStatus.OK)


@country_bp.patch('/<int:country_id>')
def patch_country(country_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    country_controller.patch(country_id, content)
    return make_response("Country updated", HTTPStatus.OK)


@country_bp.delete('/<int:country_id>')
def delete_country(country_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    country_controller.delete(country_id)
    return make_response("Country deleted", HTTPStatus.OK)


@country_bp.get('/<int:country_id>/stores')
def get_employee_stores(country_id: int) -> Response:
    """
    Gets stores where the employee works.
    :param country_id: ID of the employee
    :return: Response object with stores where the employee works
    """
    country = Country.query.get(country_id)
    return make_response(jsonify(country.get_country_stores()), HTTPStatus.OK)

