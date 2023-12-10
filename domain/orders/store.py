"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Store(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "store"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    countryid = db.Column(db.Integer, db.ForeignKey('country.id'))

    brand_stores = db.relationship('Brandstore', backref='store')
    store_employees = db.relationship('Storeemployee', backref='store')
    sales = db.relationship('Sale', backref='store')
    shipments = db.relationship('Shipment', backref='store')

    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Store({self.id}, '{self.name}', '{self.address}', '{self.countryid}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """

        # brand_stores_list = [brand_stores.put_into_dto() for brand_stores in self.brand_stores]
        # store_employees_list = [store_employees.put_into_dto() for store_employees in self.store_employees]
        # sales_list = [sales.put_into_dto() for sales in self.sales]
        # shipments_list = [shipments.put_into_dto() for shipments in self.shipments]

        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "countryid": self.countryid
            # "brand_stores_list": brand_stores_list,
            # "store_employees_list": store_employees_list,
            # "sales_list": sales_list,
            # "shipments_list": shipments_list
        }

    def get_store_employees(self) -> Dict[str, Any]:
        store_employees_list = [store_employee.employee.put_into_dto() for store_employee in self.store_employees]
        return {
            "id": self.id,
            "store_employees_list": store_employees_list
        }

    def get_store_brandstores(self) -> Dict[str, Any]:
        brandstores_list = [brand_stores.brand.put_into_dto() for brand_stores in self.brand_stores]
        return {
            "id": self.id,
            "brandstores_list": brandstores_list
        }

    def get_store_sales(self) -> Dict[str, Any]:
        sales_list = [sales.put_into_dto() for sales in self.sales]
        return {
            "id": self.id,
            "sales_list": sales_list
        }

    def get_store_shipments(self) -> Dict[str, Any]:
        shipments_list = [shipments.put_into_dto() for shipments in self.shipments]
        return {
            "id": self.id,
            "shipments_list": shipments_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Store:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Store(
            name=dto_dict.get("name"),
            address=dto_dict.get("address"),
            countryid=dto_dict.get("countryid")
        )
        return obj
