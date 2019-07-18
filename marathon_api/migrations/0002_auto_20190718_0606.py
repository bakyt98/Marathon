# Generated by Django 2.2.3 on 2019-07-18 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marathon_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='urlCompressed',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='urlOriginal',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]