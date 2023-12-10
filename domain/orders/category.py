"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Category(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

    products = db.relationship('Product', backref='category')
    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Category({self.id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        # products_list = [products.put_into_dto() for products in self.products]

        return {
            "id": self.id,
            "name": self.name
            # "products_list": products_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Category:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Category(
            name=dto_dict.get("name")
        )
        return obj

    def get_category_products(self) -> Dict[str, Any]:
        """
        Gets a list of stores where the employee works.
        :return: DTO object as dictionary with list of stores
        """
        products_list = [products.put_into_dto() for products in self.products]

        return {
            "id": self.id,
            "products_list": products_list
        }