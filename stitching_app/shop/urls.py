from django.urls import path
from shop.views import *

urlpatterns = [
    path("", home, name="home"),
    path("login/", ShopLoginView.as_view(), name="login"),
    path("logout/", ShopLogoutView.as_view(next_page='login'), name="logout"),
    path("register/", ShopRegisterView.as_view(), name="register"),
    path("order/", OrderView.as_view(), name="order"),
]
