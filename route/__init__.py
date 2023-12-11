"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask
from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.country_route import country_bp
    from .orders.customer_route import customer_bp
    from .orders.category_route import category_bp
    from .orders.supplier_route import supplier_bp
    from .orders.brand_route import brand_bp
    from .orders.webaddress_route import webaddress_bp
    from .orders.product_route import product_bp
    from .orders.brandstore_route import brandstore_bp
    from .orders.store_route import store_bp
    from .orders.employee_route import employee_bp
    from .orders.shipment_route import shipment_bp
    from .orders.sale_route import sale_bp
    from .orders.saledetails_route import saledetails_bp
    from .orders.shipmentdetails_route import shipmentdetails_bp
    from .orders.storeemployee_route import storeemployee_bp
    from .orders.employee_data_route import employee_data_bp

    app.register_blueprint(country_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(supplier_bp)
    app.register_blueprint(brand_bp)
    app.register_blueprint(brandstore_bp)
    app.register_blueprint(webaddress_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(store_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(shipment_bp)
    app.register_blueprint(sale_bp)
    app.register_blueprint(saledetails_bp)
    app.register_blueprint(shipmentdetails_bp)
    app.register_blueprint(storeemployee_bp)
    app.register_blueprint(employee_data_bp)

