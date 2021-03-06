# Generated by Django 3.2.8 on 2021-11-09 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(blank=True, max_length=64, null=True)),
                ('link', models.CharField(max_length=64)),
                ('aciklama', models.CharField(max_length=64)),
                ('olus_tarih', models.DateTimeField(auto_now_add=True)),
                ('guncelleme_tarih', models.DateTimeField(auto_now=True)),
                ('ust_kategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='category.category')),
            ],
        ),
    ]
