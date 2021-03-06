# Generated by Django 3.2.8 on 2021-11-17 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20211115_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='isim',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='urun',
            name='ust_kategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category'),
        ),
    ]
