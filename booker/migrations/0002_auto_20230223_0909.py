# Generated by Django 3.2.16 on 2023-02-23 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookvenue',
            name='campaigns',
            field=models.CharField(choices=[('Rout', 'Rout'), ('Long nameda', 'Long nameda'), ('SecondCampaignName', 'SecondCampaignName'), ('Longnameherew', 'Longnameherew')], default=1, max_length=150),
        ),
        migrations.AlterField(
            model_name='bookvenue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookvenue', to=settings.AUTH_USER_MODEL),
        ),
    ]