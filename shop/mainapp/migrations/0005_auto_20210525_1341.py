# Generated by Django 3.2.3 on 2021-05-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_rename_addres_customer_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='sd_volume',
        ),
        migrations.AddField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объем встраивамой памяти'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличие SD карты'),
        ),
    ]
