"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Customer(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "customer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    contact_info = db.Column(db.String(255))

    sales = db.relationship('Sale', backref='customer')

    def __repr__(self) -> str:
        return f"Customer({self.id}, '{self.name}', '{self.contact_info}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """

        # sales_list = [sales.put_into_dto() for sales in self.sales]

        return {
            "id": self.id,
            "name": self.name,
            "contact_info": self.contact_info
            # "sales_list": sales_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Customer:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Customer(
            name=dto_dict.get("name"),
            customer_id=dto_dict.get("customer_id"),
            contact_info=dto_dict.get("contact_info")
        )
        return obj

    def get_customer_sales(self) -> Dict[str, Any]:
        """
        Gets a list of stores where the employee works.
        :return: DTO object as dictionary with list of stores
        """
        sales_list = [sales.put_into_dto() for sales in self.sales]

        return {
            "id": self.id,
            "sales_list": sales_list
        }
