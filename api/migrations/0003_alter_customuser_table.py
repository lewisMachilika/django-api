# Generated by Django 4.2.4 on 2023-08-09 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_customuser_user_type_alter_customuser_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customuser',
            table='auth_user',
        ),
    ]