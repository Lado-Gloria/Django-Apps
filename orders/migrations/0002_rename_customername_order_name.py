# Generated by Django 4.2.1 on 2023-06-21 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customerName',
            new_name='name',
        ),
    ]
