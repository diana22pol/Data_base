"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.country_controller import CountryController
from .orders.customer_controller import CustomerController
from .orders.category_controller import CategoryController
from .orders.supplier_controller import SupplierController
from .orders.brand_controller import BrandController
from .orders.employee_controller import EmployeeController
from .orders.webaddress_controller import WebaddressController
from .orders.product_controller import ProductController
from .orders.brandstore_controller import BrandstoreController
from .orders.store_controller import StoreController
from .orders.shipment_controller import ShipmentController
from .orders.sale_controller import SaleController
from .orders.saledetails_controller import SaledetailsController
from .orders.shipmentdetails_controller import ShipmentDetailsController
from .orders.storeemployee_controller import StoreemployeeController
from .orders.employee_data_controller import EmployeeDataController

country_controller = CountryController()
customer_controller = CustomerController()
category_controller = CategoryController()
supplier_controller = SupplierController()
brand_controller = BrandController()
employee_controller = EmployeeController()
webaddress_controller = WebaddressController()
product_controller = ProductController()
brandstore_controller = BrandstoreController()
store_controller = StoreController()
shipment_controller = ShipmentController()
sale_controller = SaleController()
saledetails_controller = SaledetailsController()
shipmentdetails_controller = ShipmentDetailsController()
storeemployee_controller = StoreemployeeController()
employee_data_controller = EmployeeDataController()
