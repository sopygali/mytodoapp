# Generated by Django 4.2 on 2023-05-01 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_task_duedate_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
