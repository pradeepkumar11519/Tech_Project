# Generated by Django 4.1.4 on 2023-01-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_contests_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contests',
            name='Contest_Duration',
            field=models.CharField(blank=True, default='-', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='Days_Remaining_For_The_Contest_To_Start',
            field=models.CharField(blank=True, default='-', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='Days_Remaining_To_Register',
            field=models.CharField(blank=True, default='-', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='Entry_Price',
            field=models.IntegerField(blank=True, default='-', null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='Name_Of_Contest',
            field=models.CharField(blank=True, default='-', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='Name_Of_Website',
            field=models.CharField(blank=True, default='-', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='OnGoing',
            field=models.BooleanField(blank=True, default='-', null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='Price_Pool',
            field=models.IntegerField(blank=True, default='-', null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='Remaining_Time',
            field=models.CharField(blank=True, default='-', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='Start_Date',
            field=models.CharField(blank=True, default='-', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='Start_Time',
            field=models.CharField(blank=True, default='-', max_length=225, null=True),
        ),
    ]
