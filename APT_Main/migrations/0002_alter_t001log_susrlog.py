# Generated by Django 5.2.2 on 2025-06-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APT_Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t001log',
            name='susrlog',
            field=models.EmailField(help_text='Logins de Email', max_length=30, verbose_name='SUsrLog'),
        ),
    ]
