# Generated by Django 2.2.1 on 2019-06-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('baroda', 'baroda'), ('ahmedabad', 'ahmedabad'), ('vidhyanagar', 'vidhyanagar')], default='baroda', max_length=40),
        ),
    ]
