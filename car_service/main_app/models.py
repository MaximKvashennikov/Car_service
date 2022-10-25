from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Owner(models.Model):
    contact_name = models.CharField(verbose_name="ФИО", max_length=200, blank=True)
    phone_number = PhoneNumberField(verbose_name="Телефон")

    class Meta:
        verbose_name = "Номер телефона"
        verbose_name_plural = "Номера телефонов"

    def __str__(self):
        return f"{self.phone_number}"
