# Generated by Django 2.1.7 on 2019-04-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdatabase', '0002_auto_20190411_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='human',
            old_name='sutname',
            new_name='surname',
        ),
        migrations.AlterField(
            model_name='human',
            name='language',
            field=models.CharField(choices=[('c++', 'C++'), ('c#', 'C-sharp'), ('JS', 'JavaScript'), ('PT', 'Python'), ('JV', 'Java')], default=('c#', 'C-sharp'), max_length=10),
        ),
    ]
