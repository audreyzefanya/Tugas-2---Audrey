from django.shortcuts import render

# Create your views here.
def show_katalog(request):
    return render(request, "katalog.html")