# Generated by Django 2.2.4 on 2019-12-01 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20191125_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(help_text='Подробно: город, улица, дом, подъезд/вход, квартира/помещение', max_length=256, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='location',
            name='contact',
            field=models.CharField(help_text='Контакты для связи', max_length=256, verbose_name='Телефон, vk или telegram'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(help_text='Те, кто предоставили место проведения', max_length=256, verbose_name='Название организации или имя владельца помещения'),
        ),
    ]
