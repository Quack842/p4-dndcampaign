# Generated by Django 3.2.16 on 2023-02-14 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0002_auto_20230213_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
