from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServicesView, Payment_userView, Payment_user_detailView, Expired_paymentsView, Expired_payments_detailView

services_router = DefaultRouter()
services_router.register(r"services", ServicesView, basename="services_view")
services_router.register(r"payment_user", Payment_userView, basename="payment_user")
services_router.register(r"payment_user_detail", Payment_user_detailView, basename="payment_user_detail")
services_router.register(r"expired_payments", Expired_paymentsView, basename="expired_payments")
services_router.register(r"expired_payments_detail", Expired_payments_detailView, basename="expired_payments_detail")

urlpatterns = services_router.urls