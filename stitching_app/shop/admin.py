from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from shop.models import User
from shop.forms import ShopUserCreationForm, ShopUserChangeForm


class ShopUserAdmin(UserAdmin):
    model = User
    add_form = ShopUserCreationForm
    form = ShopUserChangeForm

    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        (_('Personal info'), {'fields': ('name', 'address', )}),
        (_('Permissions'), {
         'fields': ('is_active', 'is_staff', )}),
        (_('Important dates'), {'fields': ('last_login', )}),
    )
    add_filedsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone_no', 'address', 'is_staff', 'is_active', 'password', 'password2', ),
        }
        ),
    )

    search_fields = ('email', 'name', )
    ordering = ('email', )

    filter_horizontal = ()


# Register your models here.
admin.site.register(User, ShopUserAdmin)
admin.site.unregister(Group)
