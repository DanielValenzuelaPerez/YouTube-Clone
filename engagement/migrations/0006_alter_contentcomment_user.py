# Generated by Django 3.2.16 on 2023-01-13 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('engagement', '0005_alter_contentcomment_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
