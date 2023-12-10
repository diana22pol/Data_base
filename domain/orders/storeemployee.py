"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Storeemployee(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "storeemployee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    storeid = db.Column(db.Integer, db.ForeignKey('store.id'))
    employeeid = db.Column(db.Integer, db.ForeignKey('employee.id'))
    hiredate = db.Column(db.Date)


    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Storeemployee({self.id}, '{self.storeid}', '{self.employeeid}', '{self.hiredate}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "storeid": self.storeid,
            "employeeid": self.employeeid,
            "hiredate": self.hiredate
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Storeemployee:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Storeemployee(
            storeid=dto_dict.get("storeid"),
            employeeid=dto_dict.get("employeeid"),
            hiredate=dto_dict.get("hiredate")
        )
        return obj
