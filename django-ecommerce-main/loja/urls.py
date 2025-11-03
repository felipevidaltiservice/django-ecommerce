from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('loja/',views.loja, name="loja"),
    path('minhaconta',views.minha_conta, name="minha_conta"),
    path('login/',views.login, name="login"),
    path('carrinho/',views.carrinho, name="carrinho"),
    path('checkout/',views.checkout, name="checkout"),
]