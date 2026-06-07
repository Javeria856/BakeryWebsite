from django.urls import path
from . import views

urlpatterns = [

  path('dashboard/', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
       path('menu/', views.menu, name='menu'),
       path('feedback/', views.feedback_view, name='feedback'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
     
    path('', views.signup, name='signup'),
 path('staff/', views.staff_list, name='staff_list'),
 path('attendance/', views.attendance_list, name='attendance_list'),
path('attendance/add/', views.attendance_create, name='attendance_add'),
path('attendance/edit/<int:pk>/', views.attendance_update, name='attendance_edit'),
path('attendance/delete/<int:pk>/', views.attendance_delete, name='attendance_delete'),
 path('payroll/', views.payroll_list, name='payroll_list'),
path('payroll/add/', views.payroll_create, name='payroll_add'),
path('payroll/edit/<int:pk>/', views.payroll_update, name='payroll_edit'),
path('payroll/delete/<int:pk>/', views.payroll_delete, name='payroll_delete'),
 path('staff/add/', views.staff_create, name='staff_add'),
 path('staff/edit/<int:pk>/', views.staff_update, name='staff_edit'),
path('staff/delete/<int:pk>/', views.staff_delete, name='staff_delete'),
path('leaves/', views.leave_list, name='leave_list'),
path('leaves/add/', views.leave_create, name='leave_add'),
path('leaves/edit/<int:pk>/', views.leave_update, name='leave_edit'),
path('leaves/delete/<int:pk>/', views.leave_delete, name='leave_delete'),
path('training/', views.training_list, name='training_list'),
path('training/add/', views.training_add, name='training_add'),
path('training/edit/<int:pk>/', views.training_edit, name='training_edit'),
path('training/delete/<int:pk>/', views.training_delete, name='training_delete'),

path('inventory/', views.inventory_list, name='inventory_list'),
path('inventory/add/', views.inventory_add, name='inventory_add'),
path('inventory/edit/<int:pk>/', views.inventory_edit, name='inventory_edit'),
path('inventory/delete/<int:pk>/', views.inventory_delete, name='inventory_delete'),

path('suppliers/', views.supplier_list, name='supplier_list'),
path('suppliers/add/', views.supplier_add, name='supplier_add'),
path('suppliers/edit/<int:pk>/', views.supplier_edit, name='supplier_edit'),
path('suppliers/delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),
  path('low-stock/', views.low_stock_inventory, name='low_stock_inventory'),
path('restock/<int:item_id>/', views.restock_inventory, name='restock_inventory'),
path('stock/', views.stock_movement_list, name='stock_movement_list'),
path('stock/add/', views.stock_movement_add, name='stock_movement_add'),
path('stock/edit/<int:pk>/', views.stock_movement_edit, name='stock_movement_edit'),
path('stock/delete/<int:pk>/', views.stock_movement_delete, name='stock_movement_delete'),

path('purchase-orders/', views.purchase_order_list, name='purchase_order_list'),
path('purchase-orders/add/', views.purchase_order_add, name='purchase_order_add'),
path('purchase-orders/edit/<int:pk>/', views.purchase_order_edit, name='purchase_order_edit'),
path('purchase-orders/delete/<int:pk>/', views.purchase_order_delete, name='purchase_order_delete'),

path('purchase-orders/details/add/', views.purchase_order_detail_add, name='purchase_order_detail_add'),

# Products & Menu
path('categories/', views.category_list, name='category_list'),
path('categories/add/', views.category_add, name='category_add'),

path('products/', views.product_list, name='product_list'),
path('products/add/', views.product_add, name='product_add'),

path('customizations/', views.customization_list, name='customization_list'),
path('customizations/add/', views.customization_add, name='customization_add'),
# Category CRUD
path('categories/edit/<int:pk>/', views.category_edit, name='category_edit'),
path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

# Product CRUD
path('products/edit/<int:pk>/', views.product_edit, name='product_edit'),
path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),

# Customization CRUD
path('customizations/edit/<int:pk>/', views.customization_edit, name='customization_edit'),
path('customizations/delete/<int:pk>/', views.customization_delete, name='customization_delete'),

# Recipes
path('recipes/', views.recipe_list, name='recipe_list'),
path('recipes/add/', views.recipe_add, name='recipe_add'),
path('recipes/edit/<int:pk>/', views.recipe_edit, name='recipe_edit'),
path('recipes/delete/<int:pk>/', views.recipe_delete, name='recipe_delete'),

# Recipe Ingredients
path('recipe-ingredients/', views.recipe_ingredient_list, name='recipe_ingredient_list'),
path('recipe-ingredients/add/', views.recipe_ingredient_add, name='recipe_ingredient_add'),
path('recipe-ingredients/edit/<int:pk>/', views.recipe_ingredient_edit, name='recipe_ingredient_edit'),
path('recipe-ingredients/delete/<int:pk>/', views.recipe_ingredient_delete, name='recipe_ingredient_delete'),
# Customers
path('customers/', views.customer_list, name='customer_list'),
path('customers/add/', views.customer_add, name='customer_add'),
path('customers/edit/<int:pk>/', views.customer_edit, name='customer_edit'),
path('customers/delete/<int:pk>/', views.customer_delete, name='customer_delete'),

# Customer Addresses
path('customer-addresses/', views.customer_address_list, name='customer_address_list'),
path('customer-addresses/add/', views.customer_address_add, name='customer_address_add'),
path('customer-addresses/edit/<int:pk>/', views.customer_address_edit, name='customer_address_edit'),
path('customer-addresses/delete/<int:pk>/', views.customer_address_delete, name='customer_address_delete'),
path('feedback/', views.feedback_list, name='feedback_list'),
path('feedback/add/', views.feedback_add, name='feedback_add'),
path('feedback/edit/<int:pk>/', views.feedback_edit, name='feedback_edit'),
path('feedback/delete/<int:pk>/', views.feedback_delete, name='feedback_delete'),
# Reports
path('reports/low-stock/', views.low_stock_report, name='low_stock_report'),
path('reports/expired-items/', views.expired_items_report, name='expired_items_report'),
path(
    'reports/monthly-waste/',
    views.report_monthly_waste,
    name='report_monthly_waste'
),
# Orders
path('orders/', views.order_list, name='order_list'),
path('orders/add/',views.order_add, name='order_add'),
path('orders/edit/<int:pk>/',views.order_edit, name='order_edit'),
path('orders/delete/<int:pk>/',views.order_delete, name='order_delete'),

# Order Details
path('order-details/', views.order_detail_list, name='order_detail_list'),
path('order-details/add/', views.order_detail_add, name='order_detail_add'),
path('order-details/edit/<int:pk>/', views.order_detail_edit, name='order_detail_edit'),
path('order-details/delete/<int:pk>/', views.order_detail_delete, name='order_detail_delete'),

# Payments
path('payments/', views.payment_list, name='payment_list'),
path('payments/add/', views.payment_add, name='payment_add'),
path('payments/edit/<int:pk>/', views.payment_edit, name='payment_edit'),
path('payments/delete/<int:pk>/', views.payment_delete, name='payment_delete'),

# Payment Methods
path('payment-methods/', views.payment_method_list, name='payment_method_list'),
path('payment-methods/add/', views.payment_method_add, name='payment_method_add'),
path('payment-methods/edit/<int:pk>/', views.payment_method_edit, name='payment_method_edit'),
path('payment-methods/delete/<int:pk>/', views.payment_method_delete, name='payment_method_delete'),
   path('deliveries/', views.delivery_list, name='delivery_list'),
path('deliveries/add/', views.delivery_add, name='delivery_add'),
path('deliveries/edit/<int:pk>/',views.delivery_edit, name='delivery_edit'),
path('deliveries/delete/<int:pk>/', views.delivery_delete, name='delivery_delete'),

path('delivery-staff/', views.delivery_staff_list, name='delivery_staff_list'),
path('delivery-staff/add/', views.delivery_staff_add, name='delivery_staff_add'),
path('delivery-staff/edit/<int:pk>/', views.delivery_staff_edit, name='delivery_staff_edit'),
path('delivery-staff/delete/<int:pk>/', views.delivery_staff_delete, name='delivery_staff_delete'),
    # Delivery Routes
    path('routes/',  views.route_list, name='route_list'),
    path('routes/add/',  views.route_add, name='route_add'),
    path('routes/edit/<int:pk>/',  views.route_edit, name='route_edit'),
    path('routes/delete/<int:pk>/',  views.route_delete, name='route_delete'),

    # Delivery Tracking
    path('tracking/',  views.tracking_list, name='tracking_list'),
    path('tracking/add/',  views.tracking_add, name='tracking_add'),
    path('tracking/edit/<int:pk>/',  views.tracking_edit, name='tracking_edit'),
    path('tracking/delete/<int:pk>/',  views.tracking_delete, name='tracking_delete'),
     path('reports/', views.report_list, name='report_list'),
path('reports/add/', views.report_add, name='report_add'),

path('expenses/', views.expense_list, name='expense_list'),
path('expenses/add/', views.expense_add, name='expense_add'),
path('report-types/', views.report_type_list, name='report_type_list'),
path('report-types/add/', views.report_type_add, name='report_type_add'),
path('report-types/edit/<int:pk>/', views.report_type_edit, name='report_type_edit'),
path('report-types/delete/<int:pk>/', views.report_type_delete, name='report_type_delete'),
path('profit-loss/', views.profit_loss_list, name='profit_loss_list'),


]


