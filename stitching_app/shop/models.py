from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import IntegrityError, models
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.contrib import admin
import datetime
from shop.utils import create_new_ref_number

# Create your models here.


class ShopUserManager(BaseUserManager):
    def create_user(self, email, name, phone_no, address, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not (len(str(phone_no)) == 10):
            raise ValueError('Enter a valid phone number')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          phone_no=phone_no, address=address, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, phone_no, address, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, name, phone_no, address, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(verbose_name="Full name",
                            max_length=50, null=False)
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    phone_no_regex = RegexValidator(
        regex=r'^[0-9]{10}$', message="Enter a valid phone number")
    phone_no = models.CharField(
        validators=[phone_no_regex],
        verbose_name='Phone no (+91)',
        max_length=10, null=False, unique=True)
    address = models.TextField(max_length=300, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_no', 'address']

    objects = ShopUserManager()

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    def __str__(self,):
        return self.name + " - " + self.email


class Item(models.Model):
    class Meta:
        pass
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30, null=False, default="")
    description = models.TextField(max_length=100, default="")
    sample_url = models.URLField(max_length=300,
                                 null=False, default="https://images.unsplash.com/photo-1618932260643-eee4a2f652a6?w=300")
    estimated_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0000.00)

    def __str__(self,):
        return self.name + "@" + str(self.estimated_price)


class Color(models.Model):
    class Meta:
        pass
    id = models.AutoField(primary_key=True, unique=True)
    value = models.CharField(
        max_length=30, unique=True, null=False, default="")

    def __str__(self,):
        return str(self.value).upper()


class Material(models.Model):
    class Meta:
        pass
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30, null=False, default="")
    price_per_metre = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0000.00)

    def __str__(self,):
        return self.name + "@" + str(self.price_per_metre) + "/metre"


class AvailableMaterial(models.Model):
    mid = models.ForeignKey(
        Material, on_delete=models.CASCADE, verbose_name="Material",)
    cid = models.ForeignKey(
        Color, on_delete=models.CASCADE, verbose_name="Color",)
    available_length = models.DecimalField(
        max_digits=4, decimal_places=2, null=False, default=00.00, verbose_name="Available length (in meters)")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['mid', 'cid'], name='AvailableMaterialConstraint')
        ]
        ordering = ['available_length', ]

    def __str__(self,):
        return str(self.mid) + " - " + str(self.cid) + " - " + str(self.available_length) + " metres"


class Review(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(
        User, verbose_name="User", on_delete=models.CASCADE, editable=False)
    review = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], default=1, null=False, editable=False)
    comment = models.TextField(max_length=255, blank=True, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self,):
        return str(self.review) + " " + str(self.comment)


class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('user_id', 'review', 'comment', 'timestamp')


# class OrderSummary(models.Model):
#     class Meta:
#         pass
#     order_id = models.CharField(
#         verbose_name='Order ID', null=False, default="000000000000", editable=False, max_length=12, primary_key=True, unique=True)
#     total_amount = models.DecimalField(
#         decimal_places=2, max_digits=6, default=00000.00, null=False)

#     def set_order_id(self,):
#         self.order_id = create_new_ref_number(12)
#         return self.order_id

#     def set_order_total_amount(self, amount)
#         self.total_amount += _

#     def save(self,):
#         super().save()


# class OrderSummaryAdmin(admin.ModelAdmin):
#     readonly_fields = ('order_id', )

class Order(models.Model):
    class Meta:
        pass
    id = models.AutoField(primary_key=True, unique=True)
    order_id = models.CharField(verbose_name='Order ID', null=False,
                                default="000000000000", editable=False, max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], null=False, default=1)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    date_of_delivery = models.DateField(verbose_name="Deliver by", validators=[
        MinValueValidator(datetime.datetime.now().date()),
    ])
    worked_on_by = models.ManyToManyField('Employee', through='AssignedWork')
    total_amount = models.DecimalField(
        verbose_name="Total amount (Rs)",
        decimal_places=2, max_digits=7, default=0000.00, null=False, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self, ):
        return "ORDER # " + str(self.order_id) + " - " + str(self.user.email)

    def save(self, ):
        self.total_amount = self.item.estimated_price * self.quantity
        if self.order_id == "000000000000":
            self.order_id = create_new_ref_number(12)
            reminder = Reminder(order=self, due_date=self.date_of_delivery)
            # @TODO: Fix error when no account record exists
            account = Account.objects.first()
            account.balance += self.total_amount
            account.save()
        else:
            reminder = Reminder.objects.get(order=self)
            reminder.due_date = self.date_of_delivery
        try:
            super().save()
            reminder.save()
        except IntegrityError:
            self.save()


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_id', 'total_amount', 'timestamp', )


class Employee(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.DecimalField(
        max_digits=7, decimal_places=2, null=False, default=00000.00)
    works_on = models.ManyToManyField(
        'Order', through='AssignedWork')

    def __str__(self,):
        return "Emp - " + str(self.user.name)

    def save(self, ):
        self.user.is_staff = True
        super().save()


class AssignedWork(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self,):
        return str(self.employee) + " - " + str(self.order)


class Reminder(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    due_date = models.DateField()

    def __str__(self,):
        return str(self.order) + " - " + str(self.due_date)


class Account(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=00000000.00)
    last_updated_on = models.DateTimeField(auto_now=True)

    def __str__(self,):
        return "Rs " + str(self.balance) + " /- @ " + str(self.last_updated_on)
