from django.shortcuts import render
from .models import *
from django.views.generic import DetailView
# Create your views here.

def categoryview(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'category.html', context)



def UrunDetail(request, id):
    context = {}
    urundetail = Urun.objects.filter(ust_kategory_id=id, active=True)
    context['urundetail'] = urundetail
    context['categories'] = Category.objects.all()
    return render(request, "urun.html", context=context)




def urunview(request):
    context = {}
    context['categories'] = Category.objects.all()
    context['urunler'] = Urun.objects.all()
    return render(request, 'urun.html', context)








class UrunDetailView(DetailView):
    model = Urun
    context_object_name = 'urun'
    template_name = 'urundetail.html'





# def producdetailview(request, id,*args,**kwargs):
#     urundetail = Urun.objects.filter(ust_kategory_id=id)
#     # categories = Urun.objects.all()
#     context = {
#
#         'uruns': urundetail,
#         # 'categories': categories
#     }
#     return render(request, "product_detail.html",context)