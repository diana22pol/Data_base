"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Webaddress(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "webaddresse"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255))
    branstoreid = db.Column(db.Integer, db.ForeignKey('brandstore.id'))

    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Webaddress({self.id}, '{self.url}', '{self.branstoreid}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "url": self.url,
            "branstoreid": self.branstoreid
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Webaddress:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Webaddress(
            url=dto_dict.get("url"),
            branstoreid=dto_dict.get("branstoreid")
        )
        return obj
