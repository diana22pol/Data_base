"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Supplier(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "supplier"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    suppliername = db.Column(db.String(255))
    contactinfo = db.Column(db.String(255))

    shipments = db.relationship('Shipment', backref='supplier')
    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Supplier({self.id}, '{self.suppliername}', '{self.contactinfo}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        # shipments_list = [shipments.put_into_dto() for shipments in self.shipments]

        return {
            "id": self.id,
            "suppliername": self.suppliername,
            "contactinfo": self.contactinfo
            # "shipments_list": shipments_list
        }

    def get_supplier_shipments(self) -> Dict[str, Any]:
        """
        Gets a list of stores where the employee works.
        :return: DTO object as dictionary with list of stores
        """
        shipments_list = [shipments.put_into_dto() for shipments in self.shipments]

        return {
            "id": self.id,
            "shipments_list": shipments_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Supplier:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Supplier(
            suppliername=dto_dict.get("suppliername"),
            contactinfo=dto_dict.get("contactinfo")
        )
        return obj
