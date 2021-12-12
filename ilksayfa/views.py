from django.shortcuts import render
from category.models import *



def indexview(request):
    return render(request, "index.html")


def contactview(request):
    return render(request, "contact.html")





