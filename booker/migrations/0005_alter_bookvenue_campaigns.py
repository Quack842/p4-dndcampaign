# Generated by Django 3.2.16 on 2023-05-20 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0004_alter_bookvenue_campaigns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookvenue',
            name='campaigns',
            field=models.CharField(choices=[('NewOnese', 'NewOnese'), ('Lst', 'Lst'), ('Lest Hope its done', 'Lest Hope its done'), ('CreatingCampaignfottest', 'CreatingCampaignfottest'), ('HPLEASE', 'HPLEASE'), ('IbegYou', 'IbegYou'), ('PLEEASSE', 'PLEEASSE'), ('KeepingItUp', 'KeepingItUp'), ('NowWe Hope', 'NowWe Hope'), ('HopefullyLastTest', 'HopefullyLastTest'), ('LizzysGang', 'LizzysGang'), ('QuackersSquad', 'QuackersSquad'), ('HopeLost', 'HopeLost'), ('The Dragons', 'The Dragons'), ('Dragon Masters', 'Dragon Masters'), ('HopeTrusters', 'HopeTrusters'), ('Johns', 'Johns'), ("Harry's Campaign", "Harry's Campaign"), ('Long nameda', 'Long nameda'), ('SecondCampaignName', 'SecondCampaignName')], default=None, max_length=150, unique=True),
        ),
    ]
