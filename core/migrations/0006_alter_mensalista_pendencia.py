# Generated by Django 4.0.2 on 2022-05-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_mensalista_pendencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalista',
            name='pendencia',
            field=models.BooleanField(blank=True, null=True, verbose_name='Pendência'),
        ),
    ]
