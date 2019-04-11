# Generated by Django 2.1.7 on 2019-04-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationmodels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name="Ім'я")),
                ('surname', models.CharField(max_length=15, verbose_name='Прізвище')),
                ('birthday', models.DateField()),
            ],
        ),
    ]