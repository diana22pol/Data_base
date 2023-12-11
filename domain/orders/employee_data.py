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


class EmployeeData(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "employee_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.Integer)
    residence = db.Column(db.String(255))

    def __repr__(self) -> str:
        return f"Employee({self.id}, '{self.employee_id}', '{self.residence}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """

        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "residence": self.residence
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EmployeeData:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = EmployeeData(
            id=dto_dict.get("id"),
            employee_id=dto_dict.get("employee_id"),
            residence=dto_dict.get("residence")
        )
        return obj
