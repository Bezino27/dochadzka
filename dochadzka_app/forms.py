from unicodedata import category

from django import forms

from dochadzka_app.models import Player, Category, Training

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields= ['jersey_number', 'first_name', 'last_name', 'birth_date', 'email_1', 'email_2', 'categories']
        widgets = {
            'jersey_number': forms.TextInput(attrs={'type': 'number'}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'categories': forms.CheckboxSelectMultiple(),
            'email_1': forms.EmailInput(attrs={'required': False}),
        }

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['category', 'day', 'date', 'time', 'players']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'players': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        category_name = kwargs.pop('category_name', None)
        super().__init__(*args, **kwargs)

        if category_name:
            # Získať kategóriu podľa názvu a nastaviť ju ako hodnotu pre field 'category'
            category = Category.objects.get(name=category_name)
            self.fields['category'].initial = category
            # Filtrovať hráčov podľa tejto kategórie
            self.fields['players'].queryset = Player.objects.filter(categories=category)