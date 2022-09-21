from django.test import TestCase, Client
from mywatchlist.views import show_json
from mywatchlist.views import show_XML
from mywatchlist.views import show_movielink
from django.test import reverse


# Testing untuk URL watchlist
class UnitTest(TestCase):
    # untuk HTML
    def test_url_check_html(self):
        response = Client().get(reverse("mywatchlist:mywatchlist"))
        self.assertEquals(response.status_code, 200)

    # untuk XML
    def test_url_check_XML(self):
        response = Client().get(reverse("mywatchlist:mywatchlist_xml"))
        self.assertEquals(response.status_code, 200)
    
    # untuk JSON
    def test_url_check_json(self):
        response = Client().get(reverse("mywatchlist:mywatchlist_json"))
        self.assertEquals(response.status_code, 200)