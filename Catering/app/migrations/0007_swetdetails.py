# Generated by Django 2.1.1 on 2018-11-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_functiondetails_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='swetdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sweet', models.CharField(max_length=50)),
            ],
        ),
    ]