# Generated by Django 5.2.2 on 2025-06-10 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APT_Main', '0006_delete_t001tes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='t001mai',
        ),
        migrations.AlterModelTableComment(
            name='t001log',
            table_comment='Login HomePage',
        ),
        migrations.AlterModelTable(
            name='t001log',
            table='t001log',
        ),
    ]
