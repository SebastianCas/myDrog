# Generated by Django 2.0.4 on 2018-05-29 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drogeria', '0002_auto_20180528_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inyectologia',
            name='codigo',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]