from django.contrib import admin
from django.urls import path
from category.views import *

urlpatterns = [
    path('kategory/', categoryview, name='category'),
    path('urun/', urunview, name='urun'),
    path('urun/<int:id>', UrunDetail, name="urun"),
    path('urundetail/<int:pk>', UrunDetailView.as_view(), name="urundetail"),


]