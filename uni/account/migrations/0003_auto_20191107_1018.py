# Generated by Django 2.2.4 on 2019-11-07 10:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20191107_1015'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile_of_user',
        ),
    ]
