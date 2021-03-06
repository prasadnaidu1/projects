# Generated by Django 2.1.1 on 2018-11-27 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addscity',
            name='state',
        ),
        migrations.RemoveField(
            model_name='addstate',
            name='Addcity',
        ),
        migrations.AddField(
            model_name='addscity',
            name='Add_state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.addstate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donor',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.addscity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.addscity'),
            preserve_default=False,
        ),
    ]
