# Generated by Django 2.2.4 on 2019-11-15 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_delete_profile_of_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.CharField(default='+7-xxx-xxx-xx-xx', help_text='Контакты для связи', max_length=256, verbose_name='Телефон, vk или telegram'),
        ),
    ]
