"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.controller import brand_controller
from t08_flask_mysql.app.my_project.auth.dao import brand_dao
from t08_flask_mysql.app.my_project.auth.dao.orders.brand_dao import BrandDAO
from t08_flask_mysql.app.my_project.auth.domain import Brand

brand_bp = Blueprint('brands', __name__, url_prefix='/brands')


@brand_bp.get('')
def get_all_countries() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(brand_controller.find_all()), HTTPStatus.OK)


@brand_bp.post('')
def create_category() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    brand = Brand.create_from_dto(content)
    brand_controller.create(brand)
    return make_response(jsonify(brand.put_into_dto()), HTTPStatus.CREATED)


@brand_bp.get('/<int:brand_id>')
def get_category(brand_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(brand_controller.find_by_id(brand_id)), HTTPStatus.OK)


@brand_bp.put('/<int:brand_id>')
def update_country(brand_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    brand = Brand.create_from_dto(content)
    brand_controller.update(brand_id, brand)
    return make_response("Brand updated", HTTPStatus.OK)


@brand_bp.patch('/<int:brand_id>')
def patch_country(brand_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    brand_controller.patch(brand_id, content)
    return make_response("Brand updated", HTTPStatus.OK)


@brand_bp.delete('/<int:brand_id>')
def delete_country(brand_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    brand_controller.delete(brand_id)
    return make_response("Brand deleted", HTTPStatus.OK)


@brand_bp.get('/<int:brand_id>/stores')
def get_brand_stores(brand_id: int) -> Response:
    """
    Gets stores where the employee works.
    :param brand_id: ID of the employee
    :return: Response object with stores where the employee works
    """
    brand = Brand.query.get(brand_id)
    return make_response(jsonify(brand.get_brand_stores()), HTTPStatus.OK)

@brand_bp.get('/<int:brand_id>/products')
def get_products(brand_id: int) -> Response:
    """
    Gets stores where the employee works.
    :param brand_id: ID of the employee
    :return: Response object with stores where the employee works
    """
    brand = Brand.query.get(brand_id)
    return make_response(jsonify(brand.get_products()), HTTPStatus.OK)

@brand_bp.post('/create-noname-brands')
def create_noname_brands() -> Response:
    result = brand_dao.insert_brands_with_noname()
    return make_response(jsonify(result), HTTPStatus.CREATED)