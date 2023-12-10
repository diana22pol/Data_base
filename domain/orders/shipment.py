"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Shipment(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "shipment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))

    shipment_details = db.relationship('ShipmentDetails', backref='shipment')
    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Shipment({self.id}, '{self.date}', '{self.supplier_id}', '{self.store_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        # shipment_details_list = [shipment_details.put_into_dto() for shipment_details in self.shipment_details]

        return {
            "id": self.id,
            "date": self.date,
            "supplier_id": self.supplier_id,
            "store_id": self.store_id,
            # "shipment_details_list": shipment_details_list
        }

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

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Shipment:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Shipment(
            date=dto_dict.get("date"),
            supplier_id=dto_dict.get("supplier_id"),
            store_id=dto_dict.get("store_id")
        )
        return obj
