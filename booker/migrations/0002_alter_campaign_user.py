# Generated by Django 3.2.16 on 2023-02-20 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to=settings.AUTH_USER_MODEL),
        ),
    ]