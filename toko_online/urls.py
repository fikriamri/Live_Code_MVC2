from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('barang/<int:barang_id>/', views.barang_detail, name='barang_detail'),
    path('barang/tambah/', views.barang_tambah, name='barang_tambah'),
]