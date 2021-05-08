# Generated by Django 3.1.4 on 2021-05-08 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='task',
        ),
        migrations.AddField(
            model_name='permission',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shared_task', to='tasks.task'),
        ),
        migrations.RemoveField(
            model_name='permission',
            name='user',
        ),
        migrations.AddField(
            model_name='permission',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shared_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
