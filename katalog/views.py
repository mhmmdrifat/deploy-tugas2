from django.shortcuts import render
from katalog.models import CatalogItem

def isi_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog' : data_katalog,
        'Nama'  : 'Muhammad Rifat Fadhillah',
        'student_id'    : '2106752470',
    }
    return render(request, 'katalog.html', context)
# TODO: Create your views here.
