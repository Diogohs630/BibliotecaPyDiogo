# Generated by Django 4.2.5 on 2023-09-05 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_autor_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editora',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade'),
        ),
    ]