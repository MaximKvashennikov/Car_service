from django.forms import ModelForm, Textarea
from .models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["feedback_text"]

        widgets = {
            "feedback_text": Textarea(attrs={
                "placeholder": "Напишите текст отзыва...",
                "rows": "4",
                "class": ("px-0 w-full text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 "
                          "focus:ring-0 dark:text-white dark:placeholder-gray-400")
            })
        }
