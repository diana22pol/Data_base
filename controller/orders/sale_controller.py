"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import sale_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class SaleController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = sale_service
