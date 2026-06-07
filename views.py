from django.shortcuts import render, redirect, get_object_or_404
from .models import Staff, StaffAttendance, Payroll, LeaveRequests,TrainingSessions,Inventory, Supplier,StockMovement, PurchaseOrder, PurchaseOrderDetail,ProductCategory, Product, Customization,Recipe,RecipeIngredient,Customer,CustomerAddress,Order, OrderDetail, Payment, PaymentMethod,DeliveryStaff,Delivery, DeliveryRoute,DeliveryTracking,ReportType,ProfitLoss
from .forms import StaffForm,AttendanceForm,PayrollForm,LeaveRequestForm,TrainingSessionForm,InventoryForm, SupplierForm,StockMovementForm, PurchaseOrderForm, PurchaseOrderDetailForm,ProductCategoryForm, ProductForm, CustomizationForm,RecipeForm,RecipeIngredientForm,CustomerForm,CustomerAddressForm,OrderForm, OrderDetailForm, PaymentForm, PaymentMethodForm,DeliveryStaffForm,DeliveryForm, DeliveryRouteForm,DeliveryTrackingForm,ReportTypeForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'], 
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            messages.success(request, "Account created successfully")
            return redirect('login')

    else:
        form = SignupForm()

    return render(request, 'myapp/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'myapp/login.html')


def home(request):
    return render(request, 'myapp/home.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def menu(request):
    return render(request, 'myapp/menu.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

from django.db.models import Sum
from django.utils.timezone import now
from django.db.models.functions import TruncMonth
from .models import StockMovement

def dashboard(request):
    staff_count = Staff.objects.count()
    attendance_count = StaffAttendance.objects.count()
    payroll_count = Payroll.objects.count()

    LOW_STOCK_LIMIT = 5.0
    low_stock_count = Inventory.objects.filter(
        quantity__lte=LOW_STOCK_LIMIT
    ).count()

    

    context = {
        'staff_count': staff_count,
        'attendance_count': attendance_count,
        'payroll_count': payroll_count,
        'inventory_count': Inventory.objects.count(),
        'supplier_count': Supplier.objects.count(),
        'low_stock_count': low_stock_count,
        'products_count': Product.objects.count(),

       
    }

    return render(request, 'myapp/dashboard.html', context)




def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'myapp/staff_list.html', {'staff': staff})

# ADD STAFF
def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'myapp/staff_form.html', {'form': form, 'title': 'Add Staff'})


# EDIT STAFF
def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'myapp/staff_form.html', {'form': form, 'title': 'Edit Staff'})


# DELETE STAFF
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    return render(request, 'myapp/staff_delete.html', {'staff': staff})

def attendance_list(request):
    attendance = StaffAttendance.objects.all()
    return render(request, 'myapp/attendance_list.html', {'attendance': attendance})

def attendance_list(request):
    attendance = StaffAttendance.objects.select_related('staff').all()
    return render(request, 'myapp/attendance_list.html', {'attendance': attendance})


# ADD
def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'myapp/attendance_form.html', {
        'form': form,
        'title': 'Add Attendance'
    })


# EDIT
def attendance_update(request, pk):
    record = get_object_or_404(StaffAttendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=record)
    return render(request, 'myapp/attendance_form.html', {
        'form': form,
        'title': 'Edit Attendance'
    })


# DELETE
def attendance_delete(request, pk):
    record = get_object_or_404(StaffAttendance, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('attendance_list')
    return render(request, 'myapp/attendance_delete.html', {'record': record})

def payroll_list(request):
    payroll = Payroll.objects.all()
    return render(request, 'myapp/payroll_list.html', {'payroll': payroll})



# LIST PAYROLL
def payroll_list(request):
    payrolls = Payroll.objects.select_related('staff').all()
    return render(request, 'myapp/payroll_list.html', {'payrolls': payrolls})

# ADD PAYROLL
def payroll_create(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm()
    return render(request, 'myapp/payroll_form.html', {'form': form, 'title': 'Add Payroll'})

# EDIT PAYROLL
def payroll_update(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'myapp/payroll_form.html', {'form': form, 'title': 'Edit Payroll'})

# DELETE PAYROLL
def payroll_delete(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        payroll.delete()
        return redirect('payroll_list')
    return render(request, 'myapp/payroll_delete.html', {'payroll': payroll})



# LIST
def leave_list(request):
    leaves = LeaveRequests.objects.select_related('staff').all()
    return render(request, 'myapp/leave_list.html', {'leaves': leaves})

# ADD
def leave_create(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = LeaveRequestForm()
    return render(request, 'myapp/leave_form.html', {'form': form, 'title': 'Add Leave'})

# EDIT / Approve / Reject
def leave_update(request, pk):
    leave = get_object_or_404(LeaveRequests, pk=pk)
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = LeaveRequestForm(instance=leave)
    return render(request, 'myapp/leave_form.html', {'form': form, 'title': 'Edit Leave'})

# DELETE
def leave_delete(request, pk):
    leave = get_object_or_404(LeaveRequests, pk=pk)
    if request.method == 'POST':
        leave.delete()
        return redirect('leave_list')
    return render(request, 'myapp/leave_delete.html', {'leave': leave})

def training_list(request):
    trainings = TrainingSessions.objects.all()
    return render(request, 'myapp/training_list.html', {'trainings': trainings})

def training_add(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingSessionForm()
    return render(request, 'myapp/training_form.html', {'form': form})

def training_edit(request, pk):
    training = get_object_or_404(TrainingSessions, pk=pk)
    form = TrainingSessionForm(request.POST or None, instance=training)
    if form.is_valid():
        form.save()
        return redirect('training_list')
    return render(request, 'myapp/training_form.html', {'form': form})

def training_delete(request, pk):
    training = get_object_or_404(TrainingSessions, pk=pk)
    training.delete()
    return redirect('training_list')


# INVENTORY
def inventory_list(request):
    items = Inventory.objects.all()
    return render(request, 'myapp/inventory_list.html', {'items': items})

def inventory_add(request):
    form = InventoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_list')
    return render(request, 'myapp/inventory_form.html', {'form': form})

def inventory_edit(request, pk):
    item = Inventory.objects.get(pk=pk)
    form = InventoryForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('inventory_list')
    return render(request, 'myapp/inventory_form.html', {'form': form})

def inventory_delete(request, pk):
    Inventory.objects.get(pk=pk).delete()
    return redirect('inventory_list')


# SUPPLIERS
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'myapp/supplier_list.html', {'suppliers': suppliers})

def supplier_add(request):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('supplier_list')
    return render(request, 'myapp/supplier_form.html', {'form': form})

def supplier_edit(request, pk):
    supplier = Supplier.objects.get(pk=pk)
    form = SupplierForm(request.POST or None, instance=supplier)
    if form.is_valid():
        form.save()
        return redirect('supplier_list')
    return render(request, 'myapp/supplier_form.html', {'form': form})

def supplier_delete(request, pk):
    Supplier.objects.get(pk=pk).delete()
    return redirect('supplier_list')

def low_stock_inventory(request):
    LOW_STOCK_LIMIT = 5.0

    low_stock_items = Inventory.objects.filter(quantity__lte=LOW_STOCK_LIMIT)

    return render(request, 'myapp/low_stock_inventory.html', {
        'low_stock_items': low_stock_items
    })

def restock_inventory(request, item_id):
    item = get_object_or_404(Inventory, id=item_id)

    RESTOCK_AMOUNT = 10  # you can change this
    item.quantity += RESTOCK_AMOUNT
    item.save()

def feedback_view(request):
    # Agar aap database se feedback fetch kar rahe ho:
    # feedbacks = CustomerFeedback.objects.all()
    return render(request, 'myapp/feedback.html') 

def stock_movement_list(request):
    movements = StockMovement.objects.all()
    return render(request, 'myapp/stock_movement_list.html', {'movements': movements})


def stock_movement_add(request):
    form = StockMovementForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('stock_movement_list')
    return render(request, 'myapp/stock_movement_form.html', {'form': form})

def stock_movement_edit(request, pk):
    movement = get_object_or_404(StockMovement, pk=pk)
    form = StockMovementForm(request.POST or None, instance=movement)
    if form.is_valid():
        form.save()
        return redirect('stock_movement_list')
    return render(request, 'myapp/stock_movement_form.html', {'form': form})


def stock_movement_delete(request, pk):
    movement = get_object_or_404(StockMovement, pk=pk)
    movement.delete()
    return redirect('stock_movement_list')

def purchase_order_list(request):
    orders = PurchaseOrder.objects.all()
    return render(request, 'myapp/purchase_order_list.html', {'orders': orders})


def purchase_order_add(request):
    form = PurchaseOrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('purchase_order_list')
    return render(request, 'myapp/purchase_order_form.html', {'form': form})

def purchase_order_edit(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)
    form = PurchaseOrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('purchase_order_list')
    return render(request, 'myapp/purchase_order_form.html', {'form': form})


def purchase_order_delete(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)
    order.delete()
    return redirect('purchase_order_list')

def purchase_order_detail_add(request):
    form = PurchaseOrderDetailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('purchase_order_list')
    return render(request, 'myapp/purchase_order_detail_form.html', {'form': form})

def category_list(request):
    categories = ProductCategory.objects.all()
    return render(request, 'myapp/category_list.html', {'categories': categories})


def category_add(request):
    form = ProductCategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'myapp/category_form.html', {'form': form})

# UPDATE
def category_edit(request, pk):
    category = ProductCategory.objects.get(pk=pk)
    form = ProductCategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'myapp/category_form.html', {'form': form})


# DELETE
def category_delete(request, pk):
    category = ProductCategory.objects.get(pk=pk)
    category.delete()
    return redirect('category_list')


def product_list(request):
    products = Product.objects.select_related('category')
    return render(request, 'myapp/product_list.html', {'products': products})


def product_add(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'myapp/product_form.html', {'form': form})

# UPDATE
def product_edit(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'myapp/product_form.html', {'form': form})


# DELETE
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product_list')

def customization_list(request):
    customizations = Customization.objects.select_related('product')
    return render(request, 'myapp/customization_list.html', {'customizations': customizations})


def customization_add(request):
    form = CustomizationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customization_list')
    return render(request, 'myapp/customization_form.html', {'form': form})

# UPDATE
def customization_edit(request, pk):
    customization = Customization.objects.get(pk=pk)
    form = CustomizationForm(request.POST or None, instance=customization)
    if form.is_valid():
        form.save()
        return redirect('customization_list')
    return render(request, 'myapp/customization_form.html', {'form': form})


# DELETE
def customization_delete(request, pk):
    customization = Customization.objects.get(pk=pk)
    customization.delete()
    return redirect('customization_list')
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'myapp/recipe_list.html', {'recipes': recipes})


def recipe_add(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('recipe_list')
    return render(request, 'myapp/recipe_form.html', {'form': form})


def recipe_edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('recipe_list')
    return render(request, 'myapp/recipe_form.html', {'form': form})


def recipe_delete(request, pk):
    Recipe.objects.get(pk=pk).delete()
    return redirect('recipe_list')

def recipe_ingredient_list(request):
    items = RecipeIngredient.objects.all()
    return render(request, 'myapp/recipe_ingredient_list.html', {'items': items})


def recipe_ingredient_add(request):
    form = RecipeIngredientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('recipe_ingredient_list')
    return render(request, 'myapp/recipe_ingredient_form.html', {'form': form})


def recipe_ingredient_edit(request, pk):
    item = RecipeIngredient.objects.get(pk=pk)
    form = RecipeIngredientForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('recipe_ingredient_list')
    return render(request, 'myapp/recipe_ingredient_form.html', {'form': form})


def recipe_ingredient_delete(request, pk):
    RecipeIngredient.objects.get(pk=pk).delete()
    return redirect('recipe_ingredient_list')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'myapp/customer_list.html', {'customers': customers})


def customer_add(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'myapp/customer_form.html', {'form': form})


def customer_edit(request, pk):
    customer = Customer.objects.get(pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'myapp/customer_form.html', {'form': form})


def customer_delete(request, pk):
    Customer.objects.get(pk=pk).delete()
    return redirect('customer_list')

def customer_address_list(request):
    addresses = CustomerAddress.objects.all()
    return render(request, 'myapp/customer_address_list.html', {'addresses': addresses})


def customer_address_add(request):
    form = CustomerAddressForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer_address_list')
    return render(request, 'myapp/customer_address_form.html', {'form': form})


def customer_address_edit(request, pk):
    address = CustomerAddress.objects.get(pk=pk)
    form = CustomerAddressForm(request.POST or None, instance=address)
    if form.is_valid():
        form.save()
        return redirect('customer_address_list')
    return render(request, 'myapp/customer_address_form.html', {'form': form})


def customer_address_delete(request, pk):
    CustomerAddress.objects.get(pk=pk).delete()
    return redirect('customer_address_list')

from .models import CustomerFeedback
from .forms import CustomerFeedbackForm

def feedback_list(request):
    feedbacks = CustomerFeedback.objects.select_related('customer')
    return render(request, 'myapp/feedback_list.html', {'feedbacks': feedbacks})

def feedback_add(request):
    form = CustomerFeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('feedback_list')
    return render(request, 'myapp/feedback_form.html', {'form': form})

def feedback_edit(request, pk):
    feedback = get_object_or_404(CustomerFeedback, pk=pk)
    form = CustomerFeedbackForm(request.POST or None, instance=feedback)
    if form.is_valid():
        form.save()
        return redirect('feedback_list')
    return render(request, 'myapp/feedback_form.html', {'form': form})

def feedback_delete(request, pk):
    feedback = get_object_or_404(CustomerFeedback, pk=pk)
    feedback.delete()
    return redirect('feedback_list')

from django.db.models import Sum
from django.utils.safestring import mark_safe
import json
import json
from django.utils.safestring import mark_safe

import json

def low_stock_report(request):
    items = Inventory.objects.filter(quantity__lte=10)

    labels = [i.item_name for i in items]
    data = [i.quantity for i in items]

    return render(request, 'myapp/report_low_stock.html', {
        'items': items,
        'labels': labels,
        'data': data,
    })

def expired_items_report(request):
    expired = (
        StockMovement.objects
        .filter(type='EXPIRED')
        .values('inventory__item_name')
        .annotate(total_expired=Sum('quantity'))
    )

    labels = [i['inventory__item_name'] for i in expired]
    data = [float(i['total_expired']) for i in expired]

    return render(
        request,
        'myapp/report_expired_items.html',
        {
            'labels': labels,
            'data': data
        }
    )
from django.conf import settings
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .models import StockMovement

def report_monthly_waste(request):
    waste = (
        StockMovement.objects
        .filter(type='EXPIRED')
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total_waste=Sum('quantity'))
        .order_by('month')
    )

    labels = []
    data = []
    alerts = []

    for w in waste:
        if w['month']:
            labels.append(w['month'].strftime('%b %Y'))
            total = float(w['total_waste'])
            data.append(total)

            alerts.append(
                total > settings.WASTE_ALERT_LIMIT
            )

    return render(
        request,
        'myapp/report_monthly_waste.html',
        {
            'labels': labels,
            'data': data,
            'alerts': alerts,
            'limit': settings.WASTE_ALERT_LIMIT
        }
    )

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'myapp/order_list.html', {'orders': orders})


def order_add(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'myapp/order_form.html', {'form': form, 'title': 'Add Order'})


def order_edit(request, pk):
    order = Order.objects.get(pk=pk)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'myapp/order_form.html', {'form': form, 'title': 'Edit Order'})


def order_delete(request, pk):
    Order.objects.get(pk=pk).delete()
    return redirect('order_list')

def order_detail_list(request):
    details = OrderDetail.objects.all()
    return render(request, 'myapp/order_detail_list.html', {'details': details})


def order_detail_add(request):
    form = OrderDetailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('order_detail_list')
    return render(request, 'myapp/order_detail_form.html', {'form': form, 'title': 'Add Order Detail'})


def order_detail_edit(request, pk):
    detail = OrderDetail.objects.get(pk=pk)
    form = OrderDetailForm(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()
        return redirect('order_detail_list')
    return render(request, 'myapp/order_detail_form.html', {'form': form, 'title': 'Edit Order Detail'})


def order_detail_delete(request, pk):
    OrderDetail.objects.get(pk=pk).delete()
    return redirect('order_detail_list')

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'myapp/payment_list.html', {'payments': payments})


def payment_add(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('payment_list')
    return render(request, 'myapp/payment_form.html', {'form': form, 'title': 'Add Payment'})


def payment_edit(request, pk):
    payment = Payment.objects.get(pk=pk)
    form = PaymentForm(request.POST or None, instance=payment)
    if form.is_valid():
        form.save()
        return redirect('payment_list')
    return render(request, 'myapp/payment_form.html', {'form': form, 'title': 'Edit Payment'})


def payment_delete(request, pk):
    Payment.objects.get(pk=pk).delete()
    return redirect('payment_list')
def payment_method_list(request):
    methods = PaymentMethod.objects.all()
    return render(request, 'myapp/payment_method_list.html', {'methods': methods})


def payment_method_add(request):
    form = PaymentMethodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('payment_method_list')
    return render(request, 'myapp/payment_method_form.html', {'form': form, 'title': 'Add Payment Method'})


def payment_method_edit(request, pk):
    method = PaymentMethod.objects.get(pk=pk)
    form = PaymentMethodForm(request.POST or None, instance=method)
    if form.is_valid():
        form.save()
        return redirect('payment_method_list')
    return render(request, 'myapp/payment_method_form.html', {'form': form, 'title': 'Edit Payment Method'})


def payment_method_delete(request, pk):
    PaymentMethod.objects.get(pk=pk).delete()
    return redirect('payment_method_list')

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'myapp/delivery_list.html', {'deliveries': deliveries})


def delivery_add(request):
    form = DeliveryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('delivery_list')
    return render(request, 'myapp/delivery_form.html', {'form': form})


def delivery_edit(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    form = DeliveryForm(request.POST or None, instance=delivery)
    if form.is_valid():
        form.save()
        return redirect('delivery_list')
    return render(request, 'myapp/delivery_form.html', {'form': form})


def delivery_delete(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    delivery.delete()
    return redirect('delivery_list')

def delivery_staff_list(request):
    riders = DeliveryStaff.objects.all()
    return render(request, 'myapp/delivery_staff_list.html', {'riders': riders})


def delivery_staff_add(request):
    form = DeliveryStaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('delivery_staff_list')
    return render(request, 'myapp/delivery_staff_form.html', {'form': form})


def delivery_staff_edit(request, pk):
    rider = get_object_or_404(DeliveryStaff, pk=pk)
    form = DeliveryStaffForm(request.POST or None, instance=rider)
    if form.is_valid():
        form.save()
        return redirect('delivery_staff_list')
    return render(request, 'myapp/delivery_staff_form.html', {'form': form})


def delivery_staff_delete(request, pk):
    rider = get_object_or_404(DeliveryStaff, pk=pk)
    rider.delete()
    return redirect('delivery_staff_list')

def route_list(request):
    routes = DeliveryRoute.objects.all()
    return render(request, 'myapp/route_list.html', {'routes': routes})


def route_add(request):
    form = DeliveryRouteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('route_list')
    return render(request, 'myapp/route_form.html', {'form': form})


def route_edit(request, pk):
    route = DeliveryRoute.objects.get(pk=pk)
    form = DeliveryRouteForm(request.POST or None, instance=route)
    if form.is_valid():
        form.save()
        return redirect('route_list')
    return render(request, 'myapp/route_form.html', {'form': form})


def route_delete(request, pk):
    DeliveryRoute.objects.get(pk=pk).delete()
    return redirect('route_list')

def tracking_list(request):
    tracking = DeliveryTracking.objects.all()
    return render(request, 'myapp/tracking_list.html', {'tracking': tracking})


def tracking_add(request):
    form = DeliveryTrackingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tracking_list')
    return render(request, 'myapp/tracking_form.html', {'form': form})


def tracking_edit(request, pk):
    track = DeliveryTracking.objects.get(pk=pk)
    form = DeliveryTrackingForm(request.POST or None, instance=track)
    if form.is_valid():
        form.save()
        return redirect('tracking_list')
    return render(request, 'myapp/tracking_form.html', {'form': form})


def tracking_delete(request, pk):
    DeliveryTracking.objects.get(pk=pk).delete()
    return redirect('tracking_list')

from .models import GeneratedReport, ExpenseSummary
from .forms import GeneratedReportForm, ExpenseSummaryForm
def report_list(request):
    reports = GeneratedReport.objects.all()
    return render(request, 'myapp/report_list.html', {'reports': reports})

def report_add(request):
    form = GeneratedReportForm(request.POST or None)
    if form.is_valid():
        report = form.save()
        calculate_profit_loss(report)
        return redirect('report_list')
    return render(request, 'myapp/report_form.html', {'form': form})


def expense_list(request):
    expenses = ExpenseSummary.objects.all()
    return render(request, 'myapp/expense_list.html', {'expenses': expenses})

def expense_add(request):
    form = ExpenseSummaryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('expense_list')
    return render(request, 'myapp/expense_form.html', {'form': form})
def report_type_list(request):
    types = ReportType.objects.all()
    return render(request, 'myapp/report_type_list.html', {'types': types})

def report_type_add(request):

    form = ReportTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('report_type_list')
    return render(request, 'myapp/report_type_form.html', {'form': form})

def report_type_edit(request, pk):
    obj = ReportType.objects.get(pk=pk)
    form = ReportTypeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('report_type_list')
    return render(request, 'myapp/report_type_form.html', {'form': form})

def report_type_delete(request, pk):
    ReportType.objects.get(pk=pk).delete()
    return redirect('report_type_list')
def calculate_profit_loss(report):
    start = report.start_date
    end = report.end_date

    # TOTAL SALES
    total_sales = OrderDetail.objects.filter(
        order__order_date__range=[start, end]
    ).aggregate(
        total=Sum('price')
    )['total'] or 0

    # TOTAL EXPENSES
    total_expenses = ExpenseSummary.objects.filter(
        report=report
    ).aggregate(
        total=Sum('total_expenses')
    )['total'] or 0

    # NET PROFIT
    net_profit = total_sales - total_expenses

    ProfitLoss.objects.update_or_create(
        report=report,
        defaults={
            'total_sales': total_sales,
            'total_expenses': total_expenses,
            'net_profit': net_profit
        }
    )
from django.db.models import Sum
from .models import GeneratedReport, ProfitLoss, SalesSummary, ExpenseSummary

def profit_loss_list(request):
    reports = GeneratedReport.objects.all()

    for report in reports:
        # Skip if already generated
        if ProfitLoss.objects.filter(report=report).exists():
            continue

        sales = SalesSummary.objects.filter(report=report).aggregate(
            total=Sum('total_sales')
        )['total'] or 0

        expenses = ExpenseSummary.objects.filter(report=report).aggregate(
            total=Sum('total_expenses')
        )['total'] or 0

        ProfitLoss.objects.create(
            report=report,
            total_sales=sales,
            total_expenses=expenses,
            net_profit=sales - expenses
        )

    records = ProfitLoss.objects.select_related('report')

    return render(request, 'myapp/profit_loss_list.html', {
        'records': records
    })
def feedback_view(request):
    # Agar aap database se feedback fetch kar rahe ho:
    # feedbacks = CustomerFeedback.objects.all()
    return render(request, 'myapp/feedback.html') 

