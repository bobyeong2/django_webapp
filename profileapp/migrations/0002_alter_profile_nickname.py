# Generated by Django 4.1.1 on 2022-09-17 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
