# Generated by Django 3.1.3 on 2021-01-22 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metatags', '0003_auto_20210123_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metatags',
            name='keywords',
            field=models.CharField(help_text='Писать ключевые слова через запятую (с пробелом после запятой)', max_length=255, verbose_name='Ключевые слова'),
        ),
    ]
