"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Employee


class EmployeeDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Employee

    def create_databases_and_tables(self):
        try:
            self._session.execute(text("CALL CreateDatabasesAndTables()"))
            self._session.commit()
            return "Creation successful"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"