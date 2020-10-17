# Generated by Django 3.1.1 on 2020-10-17 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digiadvert', '0006_auto_20201016_2237'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Client_T',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='Phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='TelPhone',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]