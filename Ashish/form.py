from django import forms
from .models import Furniture


class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ["owner",
                  "furniture_type",
                  "company_name",
                  "description",
                  "average_cost",
                  "image_url",
                  "minimum_rental_days",]
