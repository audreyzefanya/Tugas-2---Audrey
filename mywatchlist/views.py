from django.shortcuts import render
from mywatchlist.models import BarangWatchlist
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def show_mywatchlist(request):
    data_barang_watchlist = BarangWatchlist.objects.all()
    context = {
        'movie_list': data_barang_watchlist,
        'nama': 'Audrey Zefanya Priyambodo',
        'Student ID': '2106650443'
    }
    return render(request, "mywatchlist.html", context)

def show_XML(request):
    data = BarangWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_movielink(request):
    data_barang_watchlist = BarangWatchlist.objects.all()
    context = {
        'movie_list': data_barang_watchlist,
        'nama': 'Audrey Zefanya Priyambodo',
        'Student ID': '2106650443'
    }
    return render(request, "movielink.html", context)