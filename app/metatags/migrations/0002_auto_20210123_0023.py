# Generated by Django 3.1.3 on 2021-01-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metatags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metatags',
            name='url',
            field=models.TextField(help_text='Пример: "/about/contact/". Убедитесь, что ввели начальную и конечную косые черы.', max_length=200, unique=True, verbose_name='URL - Путь'),
        ),
    ]
