# Generated by Django 4.1.1 on 2022-10-17 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectapp', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project', to=settings.AUTH_USER_MODEL),
        ),
    ]
