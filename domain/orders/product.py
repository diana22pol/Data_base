"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Product(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    shipment_details = db.relationship('ShipmentDetails', backref='product')
    sale_details = db.relationship('SaleDetails', backref='product')

    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Product({self.id}, '{self.name}', '{self.description}', '{self.brand_id}', '{self.category_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        # shipment_details_list = [shipment_details.put_into_dto() for shipment_details in self.shipment_details]
        # sale_details_list = [sale_details.put_into_dto() for sale_details in self.sale_details]


        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "brand_id": self.brand_id,
            "category_id": self.category_id
            # "shipment_details_list": shipment_details_list
            # "sale_details_list": sale_details_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Product:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Product(
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
            brand_id=dto_dict.get("brand_id"),
            category_id=dto_dict.get("category_id"),
        )
        return obj

    def get_shipment_details(self) -> Dict[str, Any]:
        """
        Gets a list of stores where the employee works.
        :return: DTO object as dictionary with list of stores
        """
        shipment_details_list = [shipment_details.put_into_dto() for shipment_details in self.shipment_details]

        return {
            "id": self.id,
            "shipment_details_list": shipment_details_list
        }

    def get_shipment_sales(self) -> Dict[str, Any]:
        """
        Gets a list of stores where the employee works.
        :return: DTO object as dictionary with list of stores
        """
        sale_details_list = [sale_details.put_into_dto() for sale_details in self.sale_details]

        return {
            "id": self.id,
            "sale_details_list": sale_details_list
        }
