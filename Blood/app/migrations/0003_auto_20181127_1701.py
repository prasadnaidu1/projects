# Generated by Django 2.1.1 on 2018-11-27 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181127_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addscity',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='addstate',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donor',
            name='cno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='donor',
            name='password',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='cno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='password',
            field=models.IntegerField(),
        ),
    ]