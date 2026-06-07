from django import forms
from .models import Staff,StaffAttendance,Payroll,LeaveRequests,TrainingSessions,Inventory, Supplier,StockMovement, PurchaseOrder, PurchaseOrderDetail,ProductCategory, Product, Customization, Recipe,RecipeIngredient,Customer,CustomerAddress,CustomerFeedback,Delivery,DeliveryStaff
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm_password')

        if password != confirm:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'phone', 'email', 'hire_date', 'salary']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = StaffAttendance
        fields = ['staff', 'date', 'in_time', 'out_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'in_time': forms.TimeInput(attrs={'type': 'time'}),
            'out_time': forms.TimeInput(attrs={'type': 'time'}),
        }


class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['staff', 'basic_salary', 'overtime', 'deductions', 'pay_date']  # correct field names
        widgets = {
            'pay_date': forms.DateInput(attrs={'type': 'date'}),
        }
class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequests
        fields = ['staff', 'start_date', 'end_date', 'reason', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

        from .models import TrainingSessions

class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSessions
        fields = ['staff', 'topic', 'date', 'remarks']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
        fields = ['inventory', 'type', 'quantity', 'date']


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['supplier', 'order_date', 'status']


class PurchaseOrderDetailForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderDetail
        fields = ['purchase_order', 'inventory', 'quantity']
from .models import ProductCategory, Product, Customization

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['category_name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']


class CustomizationForm(forms.ModelForm):
    class Meta:
        model = Customization
        fields = ['product', 'customization_type', 'extra_cost']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['product', 'steps']


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['recipe', 'inventory', 'quantity']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']


class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = CustomerAddress
        fields = ['customer', 'address', 'city']

class CustomerFeedbackForm(forms.ModelForm):
    class Meta:
        model = CustomerFeedback
        fields = ['customer', 'rating', 'comments']
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 4}),
        }
from .models import Order, OrderDetail, Payment, PaymentMethod


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

class DeliveryStaffForm(forms.ModelForm):
    class Meta:
        model = DeliveryStaff
        fields = '__all__'

from django import forms
from .models import DeliveryRoute, DeliveryTracking

class DeliveryRouteForm(forms.ModelForm):
    class Meta:
        model = DeliveryRoute
        fields = '__all__'


class DeliveryTrackingForm(forms.ModelForm):
    class Meta:
        model = DeliveryTracking
        fields = '__all__'

from .models import GeneratedReport, ExpenseSummary,ReportType
class ReportTypeForm(forms.ModelForm):
    class Meta:
        model = ReportType
        fields = ['name']

class GeneratedReportForm(forms.ModelForm):
    class Meta:
        model = GeneratedReport
        fields = ['report_type', 'start_date', 'end_date']


class ExpenseSummaryForm(forms.ModelForm):
    class Meta:
        model = ExpenseSummary
        fields = ['report', 'total_expenses']
