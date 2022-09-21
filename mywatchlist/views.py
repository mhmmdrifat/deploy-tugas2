from django.shortcuts import render
from mywatchlist.models import watchlist
from django.http import HttpResponse
from django.core import serializers

def isi_watchlist(request):
    data_watchlist = watchlist.objects.all()
    context = {
        'list_watchlist' : data_watchlist,
        'Nama'  : 'Muhammad Rifat Fadhillah',
        'student_id'    : '2106752470',
    }
    return render(request, 'mywatchlist.html', context)
# Create your views here.
def isi_watchlist_xml(request):
    data_watchlist = watchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def isi_watchlist_json(request):
    data_watchlist = watchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")

def isi_watchlist_xml_by_id(request, id):
    data_watchlist = watchlist.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def isi_watchlist_json_by_id(request, id):
    data_watchlist = watchlist.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")