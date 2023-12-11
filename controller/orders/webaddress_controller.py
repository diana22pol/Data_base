"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import webaddress_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class WebaddressController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = webaddress_service
