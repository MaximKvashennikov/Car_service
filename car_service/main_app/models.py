from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime


class Owner(models.Model):
    contact_name = models.CharField(verbose_name="ФИО", max_length=200, blank=True)
    phone_number = PhoneNumberField(verbose_name="Телефон")

    class Meta:
        verbose_name = "Номер телефона"
        verbose_name_plural = "Номера телефонов"

    def __str__(self):
        return f"{self.phone_number}"


class Feedback(models.Model):
    feedback_text = models.TextField(verbose_name="Отзыв")
    date_create = models.DateTimeField(verbose_name="Дата создания", default=datetime.datetime.now)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.feedback_text}"
