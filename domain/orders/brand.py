"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Brand(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "brand"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    groupname = db.Column(db.String(255))

    brand_stores = db.relationship('Brandstore', backref='brand')
    products = db.relationship('Product', backref='brand')

    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Brand({self.id}, '{self.name}', '{self.groupname}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        # brand_stores_list = [brand_stores.put_into_dto() for brand_stores in self.brand_stores]
        # products_list = [products.put_into_dto() for products in self.products]

        return {
            "id": self.id,
            "name": self.name,
            "groupname": self.groupname
            # "brand_stores_list": brand_stores_list,
            # "products_list": products_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Brand:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Brand(
            name=dto_dict.get("name"),
            groupname=dto_dict.get("groupname")
        )
        return obj

    def get_brand_stores(self) -> Dict[str, Any]:
        """
        Gets a list of stores where the employee works.
        :return: DTO object as dictionary with list of stores
        """
        brand_stores_list = [brand_stores.store.put_into_dto() for brand_stores in self.brand_stores]

        return {
            "id": self.id,
            "brand_stores_list": brand_stores_list
        }

    def get_products(self) -> Dict[str, Any]:
        """
        Gets a list of stores where the employee works.
        :return: DTO object as dictionary with list of stores
        """
        products_list = [products.put_into_dto() for products in self.products]

        return {
            "id": self.id,
            "products_list": products_list
        }
