from django.urls import path
from mywatchlist.views import isi_watchlist
from mywatchlist.views import isi_watchlist_json
from mywatchlist.views import isi_watchlist_xml
from mywatchlist.views import isi_watchlist_xml_by_id
from mywatchlist.views import isi_watchlist_json_by_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', isi_watchlist, name='isi_watchlist'),
    path('html/', isi_watchlist, name='isi_watchlist'),
    path('xml/', isi_watchlist_xml, name='isi_watchlist_xml'),
    path('json/', isi_watchlist_json, name='isi_watchlist_json'),
    path('json/<int:id>', isi_watchlist_json_by_id, name='isi_watchlist_json_by_id'),
    path('xml/<int:id>', isi_watchlist_xml_by_id, name='isi_watchlist_xml_by_id'),
]