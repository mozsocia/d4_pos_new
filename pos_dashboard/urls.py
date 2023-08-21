from django.urls import path, include
from . views import *

urlpatterns = [

    path('home/', index, name='homee'),
    path('pos/', include('pos_dashboard.api.urls')),
    path('adduser/', user_add, name='add_user'),
    path('userlist/', user_list, name='user_list'),
    path('add-product', ProductCreate.as_view(), name='add_product'),
    path('product_list/', productlist, name='product_list'),

    path('supplier-add/', supplier_add, name='supplier_add'),
    path('supplier-list/', supplier_list, name='supplierlist'),

    path('purchase_product/', purchase_product, name='purchase_product'),
    path('purchase_list/', purchase_product_list, name='purchase_list'),
    path('purchase-due-list/', purchase_due_list, name='purchase_due_list'),
 
 
    #Sales product
    path('sales/product/', sales_product, name='sales_product'),
    path('sales-list/', sales_list, name='sales_list'),
    path('new-purchase-return/', new_purchase_return, name='new_purchase_return'),
    path('sales-return-list/', purchase_return_list, name='purchase_return_list'),
    path('sales-due-list/', sales_due_list, name='sales_due_list'),

    # category
    path('add-category/', category_add, name='category_add'),
    path('category-list/', category_list, name='category_list'),

    # Brand
    path('brand-add/', brand_add, name='brand_add'),
    path('brand-list/', brand_list, name='brand_list'),

    # Unit
    path('unit_add/', unit_add, name='unit_add'),
    # path('unit_list/', unit_list, name='unit_list'),
    
    # customer
    path('add_customer', add_customer, name='add_customers'),
    path('customers_list', customers_list, name='customers_list'),
    
    # quotation
    path('add_quotation', add_quotation, name='add_quotation'),
    path('quotation_list', quotation_list, name='quotation_list'),
    
    # purchase returns
    path('purchase_return_list', purchase_return_list, name='purchase_return_list'),
    path('add_purchase_return', add_purchase_return, name='add_purchase_return'),
    
    # sales returns
    path('add_sales_return', add_sales_return, name='add_sales_return'),
    path('sales_return_list', sales_return_list, name='sales_return_list'),
    

]