from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jampandu(request):
    return HttpResponse('<h1><marquee scrollamount="100px" direction="up" >hii jampandu</marquee></h1>')


def ranga(request):
    return HttpResponse('I Am Ranga')
