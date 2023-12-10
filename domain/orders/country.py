"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Country(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "country"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

    stores = db.relationship('Store', backref='country')
    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Country({self.id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        # stores_list = [stores.put_into_dto() for stores in self.stores]

        return {
            "id": self.id,
            "name": self.name
            # "stores_list": stores_list
        }

    def get_country_stores(self) -> Dict[str, Any]:
        """
        Gets a list of stores where the employee works.
        :return: DTO object as dictionary with list of stores
        """
        stores_list = [stores.put_into_dto() for stores in self.stores]

        return {
            "id": self.id,
            "stores_list": stores_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Country:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Country(
            name=dto_dict.get("name")
        )
        return obj
