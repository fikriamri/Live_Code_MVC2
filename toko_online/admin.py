from django.contrib import admin
from .models import Barang

# Register your models here.
class BarangAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama_barang', 'harga_barang', 'deskripsi', 'pic', 'tanggal_input']
    list_display_links = ['id', 'nama_barang']
    search_fields = ['nama_barang']

admin.site.register(Barang, BarangAdmin)