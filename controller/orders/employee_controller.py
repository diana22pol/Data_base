"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import employee_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class EmployeeController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = employee_service
