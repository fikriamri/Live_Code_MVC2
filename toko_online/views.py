from django.shortcuts import render, redirect, get_object_or_404
from .models import Barang
from .forms import BarangForm
from django.http import Http404

# Create your views here.
def home(request):
    list_barang = Barang.objects.all()
    return render(request, 'home.html', {'Barang': list_barang})

def barang_detail(request, barang_id):
    pass
    try:
        list_barang = Barang.objects.get(pk=barang_id)
    except Barang.DoesNotExist:
        raise Http404("Barang tidak tersedia")
    return render(request, 'barang_detail.html', {'Barang': list_barang})

def barang_tambah(request):
    if request.method == "POST":
        form = BarangForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('barang_tambah')
    else:
        form = BarangForm()
    return render(request, 'barang_tambah.html', {'form': form})