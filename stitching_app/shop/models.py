from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


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
        User, verbose_name="User", on_delete=models.CASCADE)
    review = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], default=1, null=False)
    comment = models.TextField(max_length=255, blank=True)

# class Order(models.Model):
#     class Meta:
#         pass
#     quantity = models.PositiveIntegerField(validators=[
#         MinValueValidator(1),
#         MaxValueValidator(5)
#     ], null=False, default=1)
