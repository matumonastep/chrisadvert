# Generated by Django 3.1.1 on 2020-10-16 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digiadvert', '0005_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='TelPhone',
            new_name='Phone',
        ),
    ]
