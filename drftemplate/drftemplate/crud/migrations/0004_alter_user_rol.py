# Generated by Django 4.0.2 on 2022-03-16 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rol', to='crud.rol', verbose_name='Rol'),
        ),
    ]
