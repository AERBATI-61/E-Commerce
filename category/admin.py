from django.contrib import admin

# Register your models here.
from .models import *

class Admin_category(admin.ModelAdmin):
    list_display = ["isim"]
    list_filter = ["isim"]

admin.site.register(Category, Admin_category)


class PostAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_preview',)
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(Post, PostAdmin)





class Admin_urun(admin.ModelAdmin):
    list_display = ["urun_ismi", "ust_kategory"]
    list_filter = ["urun_ismi"]

admin.site.register(Urun, Admin_urun)