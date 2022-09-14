from django.urls import path
from katalog.views import isi_katalog

nama_app = 'katalog'

urlpatterns = [
    path('', isi_katalog,name ='isi_katalog'),
]
# TODO: Implement Routings Here