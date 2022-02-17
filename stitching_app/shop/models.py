from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class ShopUserManager(BaseUserManager):
    def create_user(self, email, name, phone_no, address, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        # if not (len(str(phone_no)) == 10):
        #     raise ValueError('Enter a valid phone number')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_no=phone_no,
            address=address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_staffuser(self, email, name, phone_no, address, password):
    #     """
    #     Creates and saves a staff user with the given email and password.
    #     """
    #     user = self.create_user(
    #         email,
    #         password,
    #         name,
    #         phone_no,
    #         address,
    #     )
    #     user.staff = True
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, email, name, phone_no, address, password=None):
        user = self.create_user(
            email,
            password,
            name,
            phone_no,
            address
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    phone_no = models.CharField(
        max_length=10, null=False, unique=True)
    address = models.TextField(max_length=300, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_no', 'address']

    objects = ShopUserManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self,):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    # @property
    # def is_superuser(self,):
    #     "Is the user a member of superuser?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin

    def __str__(self,):
        return self.name + " - " + self.email
