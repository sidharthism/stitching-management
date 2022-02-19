from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.


class ShopUserManager(BaseUserManager):
    # class Meta:
    #     model = User
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

    # def create_superuser(self, email, name, phone_no, address, password=None):
    #     user = self.create_user(
    #         email,
    #         password,
    #         name,
    #         phone_no,
    #         address
    #     )
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user

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
    # is_admin = models.BooleanField(default=False)
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

    # @property
    # def is_staff(self,):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin

    # @property
    # def is_superuser(self,):
    #     "Is the user a member of superuser?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin

    def __str__(self,):
        return self.name + " - " + self.email
