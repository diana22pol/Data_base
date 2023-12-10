"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Sale(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "sale"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))

    sale_details = db.relationship('SaleDetails', backref='sale')
    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Sale({self.id}, '{self.date}', '{self.customer_id}', '{self.store_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        # sale_details_list = [sale_details.put_into_dto() for sale_details in self.sale_details]

        return {
            "id": self.id,
            "date": self.date,
            "customer_id": self.customer_id,
            "store_id": self.store_id
            # "sale_details_list": sale_details_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Sale:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Sale(
            date=dto_dict.get("date"),
            customer_id=dto_dict.get("customer_id"),
            store_id=dto_dict.get("store_id")
        )
        return obj

    def get_sales_details(self) -> Dict[str, Any]:
        """
        Gets a list of stores where the employee works.
        :return: DTO object as dictionary with list of stores
        """
        sale_details_list = [sale_details.put_into_dto() for sale_details in self.sale_details]

        return {
            "id": self.id,
            "sale_details_list": sale_details_list
        }
