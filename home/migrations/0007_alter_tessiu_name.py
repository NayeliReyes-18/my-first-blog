# Generated by Django 3.2.7 on 2021-10-22 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211021_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tessiu',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.paciente', verbose_name='nombre'),
        ),
    ]
