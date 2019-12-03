# Generated by Django 2.2.7 on 2019-12-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={},
        ),
        migrations.AlterModelManagers(
            name='client',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='client_id',
        ),
        migrations.AddField(
            model_name='client',
            name='client_username',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]