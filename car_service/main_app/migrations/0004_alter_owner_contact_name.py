# Generated by Django 4.1.1 on 2022-10-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0003_alter_owner_contact_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="owner",
            name="contact_name",
            field=models.CharField(blank=True, max_length=200, verbose_name="ФИО"),
        ),
    ]
