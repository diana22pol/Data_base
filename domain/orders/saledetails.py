"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class SaleDetails(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "saledetails"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    saleid = db.Column(db.Integer, db.ForeignKey('sale.id'))
    productid = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)


    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Saledetails({self.id}, '{self.saleid}', '{self.productid}', '{self.quantity}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "saleid": self.saleid,
            "productid": self.productid,
            "quantity": self.quantity
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SaleDetails:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = SaleDetails(
            saleid=dto_dict.get("saleid"),
            productid=dto_dict.get("productid"),
            quantity=dto_dict.get("quantity")
        )
        return obj
