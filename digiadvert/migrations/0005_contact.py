# Generated by Django 3.1.1 on 2020-10-16 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digiadvert', '0004_auto_20201016_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TelPhone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='digiadvert.address')),
            ],
        ),
    ]
