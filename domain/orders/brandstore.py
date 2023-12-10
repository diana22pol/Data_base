"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Brandstore(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "brandstore"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brandid = db.Column(db.Integer, db.ForeignKey('brand.id'))
    storeid = db.Column(db.Integer, db.ForeignKey('store.id'))
    openingdate = db.Column(db.Date)

    web_addresses = db.relationship('Webaddress', backref='brandstore')

    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Brandstore({self.id}, '{self.brandid}', '{self.storeid}', '{self.openingdate}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        # web_addresses_list = [web_addresses.put_into_dto() for web_addresses in self.web_addresses]

        return {
            "id": self.id,
            "brandid": self.brandid,
            "storeid": self.storeid,
            "openingdate": self.openingdate
            # "web_addresses_list": web_addresses_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Brandstore:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Brandstore(
            brandid=dto_dict.get("brandid"),
            storeid=dto_dict.get("storeid"),
            openingdate=dto_dict.get("openingdate")
        )
        return obj

    def get_web_addresses(self) -> Dict[str, Any]:
        """
        Gets a list of stores where the employee works.
        :return: DTO object as dictionary with list of stores
        """
        web_addresses_list = [web_addresses.put_into_dto() for web_addresses in self.web_addresses]

        return {
            "id": self.id,
            "web_addresses_list": web_addresses_list
        }