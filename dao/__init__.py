"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.country_dao import CountryDAO
from .orders.customer_dao import CustomerDAO
from .orders.category_dao import CategoryDAO
from .orders.supplier_dao import SupplierDAO
from .orders.brand_dao import BrandDAO
from .orders.employee_dao import EmployeeDAO
from .orders.webaddress_dao import WebaddressDAO
from .orders.product_dao import ProductDAO
from .orders.brandstore_dao import BrandstoreDAO
from .orders.store_dao import StoreDAO
from .orders.shipment_dao import ShipmentDAO
from .orders.sale_dao import SaleDAO
from .orders.saledetails_dao import SaledetailsDAO
from .orders.shipmentdetails_dao import ShipmentDetailsDAO
from .orders.storeemployee_dao import StoreemployeeDAO
from .orders.employee_data_dao import EmployeeDataDAO

country_dao = CountryDAO()
customer_dao = CustomerDAO()
category_dao = CategoryDAO()
supplier_dao = SupplierDAO()
brand_dao = BrandDAO()
employee_dao = EmployeeDAO()
webaddress_dao = WebaddressDAO()
product_dao = ProductDAO()
brandstore_dao = BrandstoreDAO()
store_dao = StoreDAO()
shipment_dao = ShipmentDAO()
sale_dao = SaleDAO()
saledetails_dao = SaledetailsDAO()
shipmentdetails_dao = ShipmentDetailsDAO()
storeemployee_dao = StoreemployeeDAO()
employee_data_dao = EmployeeDataDAO()
