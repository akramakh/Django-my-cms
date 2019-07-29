
from django.urls import path
from . import views

urlpatterns = [
    path('/<int:pk>', views.portfolio_detail, name="portfolio_detail"),
    path('/modal/<int:pk>', views.modal_portfolio_detail, name="modal_portfolio_detail"),
]
