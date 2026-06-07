from django.db import models
from django.utils import timezone

class StaffRoles(models.Model):
    role_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.role_name


class Staff(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    role = models.ForeignKey(StaffRoles, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class StaffAttendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    in_time = models.TimeField()
    out_time = models.TimeField()

    def __str__(self):
        return f"{self.staff.name} - {self.date}"


class StaffShifts(models.Model):
    SHIFT_CHOICES = [
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),
    ]
    shift_name = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.shift_name


class StaffPerformance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    rating = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.staff.name} - {self.month}"


class Payroll(models.Model):
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    basic_salary = models.FloatField()
    overtime = models.FloatField(default=0)
    deductions = models.FloatField(default=0)
    net_salary = models.FloatField(blank=True)
    pay_date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Automatic net_salary calculation
        self.net_salary = self.basic_salary + self.overtime - self.deductions
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.staff.name} - {self.pay_date}"


class LeaveRequests(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.staff.name} - {self.status}"


class TrainingSessions(models.Model):
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    date = models.DateField()
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.topic} - {self.staff.name}"

from django.db import models

class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.item_name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name
    
    # =========================
# Inventory Extensions
# =========================

class StockMovement(models.Model):
    MOVEMENT_TYPES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
        ('EXPIRED', 'Expired'),
    ]

    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=MOVEMENT_TYPES)
    quantity = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.inventory.item_name} - {self.type}"


class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Received', 'Received'),
    ]

    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    order_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"PO #{self.id} - {self.supplier.name}"


class PurchaseOrderDetail(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.inventory.item_name} ({self.quantity})"

# =========================
# Products & Menu
# =========================

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customization(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customization_type = models.CharField(max_length=100)
    extra_cost = models.FloatField()

    def __str__(self):
        return f"{self.customization_type} - {self.product.name}"

class Recipe(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    steps = models.TextField()

    def __str__(self):
        return self.product.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.inventory.item_name} - {self.quantity}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.customer.name} - {self.city}"

class CustomerFeedback(models.Model):
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )
    rating = models.IntegerField()  # 1–5
    comments = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.rating}★"
class PaymentMethod(models.Model):
    method_name = models.CharField(max_length=50)

    def __str__(self):
        return self.method_name


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    order_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Order #{self.id}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateField()
    method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
class Delivery(models.Model):
    STATUS_CHOICES = [
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Failed', 'Failed'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Delivery #{self.id} - {self.status}"

class DeliveryStaff(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    vehicle_no = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.staff.name} ({self.vehicle_no})"

class DeliveryRoute(models.Model):
    route_name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.route_name


class DeliveryTracking(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.delivery} - {self.status}"

class ReportType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GeneratedReport(models.Model):
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type.name} ({self.start_date} - {self.end_date})"


class SalesSummary(models.Model):
    report = models.OneToOneField(GeneratedReport, on_delete=models.CASCADE)
    total_orders = models.IntegerField()
    total_sales = models.FloatField()


class ExpenseSummary(models.Model):
    report = models.OneToOneField(GeneratedReport, on_delete=models.CASCADE)
    total_expenses = models.FloatField()


class ProfitLoss(models.Model):
    report = models.OneToOneField(GeneratedReport, on_delete=models.CASCADE)
    total_sales = models.FloatField()
    total_expenses = models.FloatField()
    net_profit = models.FloatField()
