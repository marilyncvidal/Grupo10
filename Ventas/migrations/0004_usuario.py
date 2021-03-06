# Generated by Django 3.1.3 on 2020-11-23 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0003_auto_20201123_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(help_text='Ingrese el nombre del Productos', max_length=200)),
                ('privilegio', models.CharField(blank=True, choices=[('c', 'Cliente'), ('a', 'Administrador'), ('v', 'Ventas')], default='c', help_text='Tipo de cliente', max_length=1)),
                ('contrasena', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Ventas.categoria')),
            ],
        ),
    ]
