"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import category_controller
from t08_flask_mysql.app.my_project.auth.domain import Category

category_bp = Blueprint('categories', __name__, url_prefix='/categories')


@category_bp.get('')
def get_all_countries() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(category_controller.find_all()), HTTPStatus.OK)


@category_bp.post('')
def create_category() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    category = Category.create_from_dto(content)
    category_controller.create(category)
    return make_response(jsonify(category.put_into_dto()), HTTPStatus.CREATED)


@category_bp.get('/<int:category_id>')
def get_category(category_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(category_controller.find_by_id(category_id)), HTTPStatus.OK)


@category_bp.put('/<int:category_id>')
def update_category(category_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    category = Category.create_from_dto(content)
    category_controller.update(category_id, category)
    return make_response("Category updated", HTTPStatus.OK)


@category_bp.patch('/<int:category_id>')
def patch_category(category_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    category_controller.patch(category_id, content)
    return make_response("Category updated", HTTPStatus.OK)


@category_bp.delete('/<int:category_id>')
def delete_category(category_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    category_controller.delete(category_id)
    return make_response("Category deleted", HTTPStatus.OK)


@category_bp.get('/<int:category_id>/products')
def get_category_products(category_id: int) -> Response:
    """
    Gets stores where the employee works.
    :param category_id: ID of the employee
    :return: Response object with stores where the employee works
    """
    category = Category.query.get(category_id)
    return make_response(jsonify(category.get_category_products()), HTTPStatus.OK)
