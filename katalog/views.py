# pengambilan data dari database
from django.shortcuts import render
from katalog.models import CatalogItem

# memanggil fungsi dan menyimpan hasil query ke database
# TODO: Create your views here.
def show_katalog(request):
    data_item_catalog = CatalogItem.objects.all()
    context = {
    'item_katalog': data_item_catalog,
}
    return render(request, "katalog.html", context)