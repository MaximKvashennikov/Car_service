# Generated by Django 4.1.1 on 2022-10-25 12:56

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="owner",
            options={
                "verbose_name": "Номер телефона",
                "verbose_name_plural": "Номера телефонов",
            },
        ),
        migrations.AlterField(
            model_name="owner",
            name="contact_name",
            field=models.CharField(max_length=200, null=True, verbose_name="ФИО"),
        ),
        migrations.AlterField(
            model_name="owner",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None, verbose_name="Телефон"
            ),
        ),
    ]
