from django import forms

from dochadzka_app.models import Player


class PlayerForm(forms.Form):
    jersey_number = forms.IntegerField()  # Číslo dresu (unikátnosť sa kontroluje inde)
    first_name = forms.CharField(max_length=50)  # Krstné meno hráča
    last_name = forms.CharField(max_length=50)  # Priezvisko hráča
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Dátum narodenia hráča
    email_1 = forms.EmailField()  # Primárny email (unikátnosť sa kontroluje inde)
    email_2 = forms.EmailField(required=False)  # Sekundárny email (nepovinné)

class TrainingForm(forms.Form):
    category_name = forms.CharField(max_length=50)
    day = forms.CharField(max_length=50)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    player = forms.ModelMultipleChoiceField(
        queryset=Player.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
