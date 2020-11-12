# Generated by Django 3.0.5 on 2020-08-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200810_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='time',
            field=models.TimeField(null=True, verbose_name='%H:%M:%S'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='date',
            field=models.DateField(verbose_name='%d-%m-%Y'),
        ),
    ]
