from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import PositiveIntegerField
from datetime import date
from django.utils import timezone

# Create your models here.
class Barang(models.Model):
    nama_barang = models.CharField(max_length=255)
    harga_barang = models.PositiveIntegerField(default=0)
    deskripsi = models.TextField(max_length=1000)
    pic = models.CharField(max_length=255)
    tanggal_input = models.DateField(auto_now=True)

    def __str__(self):
        return self.nama_barang