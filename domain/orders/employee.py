"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.store import Store


class Employee(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    position = db.Column(db.String(255))
    hiredate = db.Column(db.Date)

    employee_stores = db.relationship('Storeemployee', backref='employee')
    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Employee({self.id}, '{self.name}', '{self.position}', '{self.hiredate}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        # storeemployees_list = [storeemployees.put_into_dto() for storeemployees in self.employee_stores]

        return {
            "id": self.id,
            "name": self.name,
            "position": self.position,
            "hiredate": self.hiredate,
            # "storeemployees_list": storeemployees_list
        }

    def get_employee_stores(self) -> Dict[str, Any]:
        """
        Gets a list of stores where the employee works.
        :return: DTO object as dictionary with list of stores
        """
        stores_list = [storeemployee.store.put_into_dto() for storeemployee in self.employee_stores]

        return {
            "id": self.id,
            "stores_list": stores_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Employee:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Employee(
            name=dto_dict.get("name"),
            position=dto_dict.get("position"),
            hiredate=dto_dict.get("hiredate")
        )
        return obj
