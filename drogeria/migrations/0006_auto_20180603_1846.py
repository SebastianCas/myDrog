# Generated by Django 2.0.4 on 2018-06-03 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drogeria', '0005_auto_20180528_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inyectologia',
            name='medicamento',
        ),
        migrations.RemoveField(
            model_name='inyectologia',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='inyectologia',
            name='sede',
        ),
        migrations.DeleteModel(
            name='Inyectologia',
        ),
    ]
