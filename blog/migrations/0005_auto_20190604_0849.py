# Generated by Django 2.2.1 on 2019-06-04 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190518_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.CharField(choices=[('40', '40'), ('45', '45'), ('50', '50'), ('55', '55'), ('60', '60'), ('70', '70'), ('80', '80')], default='40', max_length=3),
        ),
    ]
