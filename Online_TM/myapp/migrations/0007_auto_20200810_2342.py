# Generated by Django 3.0.5 on 2020-08-10 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200810_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='date',
            field=models.DateField(verbose_name="['%d-%m-%Y']"),
        ),
    ]