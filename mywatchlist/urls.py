from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_XML
from mywatchlist.views import show_json
from mywatchlist.views import show_movielink

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_movielink, name='show_movielink'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_XML, name='show_XML'),
    path('json/', show_json, name='show_json'),
]