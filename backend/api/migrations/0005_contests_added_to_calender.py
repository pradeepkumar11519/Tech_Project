# Generated by Django 4.1.4 on 2023-01-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_contests_contest_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='contests',
            name='Added_To_Calender',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
