from django import forms

class PlayerForm(forms.Form):
    jersey_number = forms.IntegerField()  # Číslo dresu (unikátnosť sa kontroluje inde)
    first_name = forms.CharField(max_length=50)  # Krstné meno hráča
    last_name = forms.CharField(max_length=50)  # Priezvisko hráča
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Dátum narodenia hráča
    email_1 = forms.EmailField()  # Primárny email (unikátnosť sa kontroluje inde)
    email_2 = forms.EmailField(required=False)  # Sekundárny email (nepovinné)