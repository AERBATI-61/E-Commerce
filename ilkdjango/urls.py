from django.contrib import admin
from django.urls import path, include
from ilksayfa .views import *
from user.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexview, name='index'),
    path('', include('user.urls')),
    path('', include('category.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('contact/', contactview, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
