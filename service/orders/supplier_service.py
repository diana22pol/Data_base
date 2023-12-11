"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import supplier_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class SupplierService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = supplier_dao
