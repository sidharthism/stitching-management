from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from shop.models import *
from shop.forms import ShopUserCreationForm, ShopUserChangeForm


class ShopUserAdmin(admin.ModelAdmin):
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
admin.site.register(Item)
admin.site.register(Material)
admin.site.register(Color)
admin.site.register(AvailableMaterial)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Employee)
admin.site.register(AssignedWork)
admin.site.register(Reminder)
admin.site.register(Account)
