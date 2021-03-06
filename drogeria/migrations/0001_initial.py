# Generated by Django 2.0.3 on 2018-05-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inyectologia',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('identificacion', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('receta', models.CharField(max_length=50)),
                ('medicamento', models.ForeignKey(on_delete='Cascade', to='drogeria.Medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='sede',
            field=models.ForeignKey(on_delete='Cascade', to='drogeria.Sede'),
        ),
        migrations.AddField(
            model_name='inyectologia',
            name='medicamento',
            field=models.ForeignKey(on_delete='Cascade', to='drogeria.Medicamento'),
        ),
        migrations.AddField(
            model_name='inyectologia',
            name='paciente',
            field=models.ForeignKey(on_delete='Cascade', to='drogeria.Paciente'),
        ),
        migrations.AddField(
            model_name='inyectologia',
            name='sede',
            field=models.ForeignKey(on_delete='Cascade', to='drogeria.Sede'),
        ),
    ]
