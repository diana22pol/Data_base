"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class ShipmentDetails(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "shipmentdetails"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    shipment_id = db.Column(db.Integer, db.ForeignKey('shipment.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.String(255))

    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"ShipmentDetails({self.id}, '{self.shipment_id}', '{self.product_id}', '{self.quantity}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "shipment_id": self.shipment_id,
            "product_id": self.product_id,
            "quantity": self.quantity
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ShipmentDetails:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ShipmentDetails(
            shipment_id=dto_dict.get("shipment_id"),
            product_id=dto_dict.get("product_id"),
            quantity=dto_dict.get("quantity")
        )
        return obj
