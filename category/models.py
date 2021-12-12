from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    isim                = models.CharField(max_length=64)
    def __str__(self):
        return self.isim
    # slug                = models.SlugField(allow_unicode=True)
    # link                = models.CharField(max_length=64)
    # aciklama            = models.CharField(max_length=64)
    # olus_tarih          = models.DateTimeField(auto_now_add=True)
    # guncelleme_tarih    = models.DateTimeField(auto_now=True)
    # ust_kategory        = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    #
    # def __str__(self):
    #     full_path = [self.isim]
    #     k = self.ust_kategory
    #     while k is not None:
    #         full_path.append(k.isim)
    #         k = k.ust_kategory
    #     return '.'.join(full_path[::-1])


class Post(models.Model):
    isim = models.CharField(null=True, max_length=100)
    thumbnail = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.thumbnail.url))
        return self.isim


# class urun(models.Model):
#     urun_isim = models.CharField(max_length=200, verbose_name="Ürün İsmi")
#     ust_category = models.ForeignKey(category, null=False, on_delete=models.CASCADE)
#     resim = models.ImageField(upload_to='images/', null=False)
#     image_galery = models.ManyToManyField(Post, help_text="resim galerisi")
#
#     def __str__(self):
#         return self.urun_isim


class Urun(models.Model):
    choices             = [
        ('Dollar', "Dollar"),
        ('TL', 'TL'),
        ('Euro', 'Euro')
    ]
    urun_ismi           = models.CharField(max_length=64, null=True, blank=True)
    fiyat               = models.IntegerField()
    fiyat_birimi        = models.CharField(max_length=8, choices=choices)
    indirim             = models.IntegerField()
    asil_fiyat          = models.IntegerField()
    active              = models.BooleanField(default=False)
    image               = models.ImageField(upload_to='urun/', blank=True, null=True)
    aciklama            = models.TextField()
    ust_kategory        = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    image_gallery        = models.ManyToManyField(Post, help_text="resim galerisi")
    description = RichTextUploadingField(null=True)

    def __str__(self):
        return self.urun_ismi



# isism soyisim, tel, plaka




