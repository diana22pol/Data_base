"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import webaddress_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class WebaddressService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = webaddress_dao
