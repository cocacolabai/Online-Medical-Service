# Generated by Django 3.0.5 on 2020-08-10 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200808_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='date',
            field=models.DateField(verbose_name='%Y-%m-%d'),
        ),
    ]
