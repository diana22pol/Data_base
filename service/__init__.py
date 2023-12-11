"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.country_service import CountryService
from .orders.customer_service import CustomerService
from .orders.category_service import CategoryService
from .orders.supplier_service import SupplierService
from .orders.brand_service import BrandService
from .orders.employee_service import EmployeeService
from .orders.webaddress_service import WebaddressService
from .orders.product_service import ProductService
from .orders.brandstore_service import BrandstoreService
from .orders.store_service import StoreService
from .orders.shipment_service import ShipmentService
from .orders.sale_service import SaleService
from .orders.saledetails_service import SaledetailsService
from .orders.shipmentdetails_service import ShipmentDetailsService
from .orders.storeemployee_service import StoreemployeeService
from .orders.employee_data_service import EmployeeDataService

country_service = CountryService()
customer_service = CustomerService()
category_service = CategoryService()
supplier_service = SupplierService()
brand_service = BrandService()
employee_service = EmployeeService()
webaddress_service = WebaddressService()
product_service = ProductService()
brandstore_service = BrandstoreService()
store_service = StoreService()
shipment_service = ShipmentService()
sale_service = SaleService()
saledetails_service = SaledetailsService()
shipmentdetails_service = ShipmentDetailsService()
storeemployee_service = StoreemployeeService()
employee_data_service = EmployeeDataService()