from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
# from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from shop.forms import *
from shop.models import *
# Create your views here.


class ShopLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class ShopLogoutView(LogoutView):
    pass


class ShopRegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = ShopUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(ShopRegisterView, self).form_valid(form)

# @csrf_protect


@csrf_exempt
def home(request):
    # csrfContext = RequestContext(request)
    ctx = {"review_success": None}
    if request.method == 'POST':
        review = int(request.POST.get('review', 1))
        comment = str(request.POST.get('comment', ""))
        try:
            r = Review(user_id=request.user, review=review, comment=comment)
            r.save()
            ctx["review_success"] = "Thank you for the review! Keep shopping!"
        except Exception as e:
            print(e)
    return render(request, "shop/index.html", ctx)


class OrderView(View, ):
    def get(self, request, *args, **kwargs):
        return render(request, "shop/order.html", {})


class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "shop/dashboard.html", {})
