# Generated by Django 4.1.4 on 2023-01-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_contests_added_to_calender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contests',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]