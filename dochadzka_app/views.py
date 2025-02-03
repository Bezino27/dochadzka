from lib2to3.fixes.fix_input import context
from unicodedata import category

from django.contrib import messages
from django.views.generic import TemplateView, FormView
from rest_framework.templatetags.rest_framework import TRAILING_PUNCTUATION

from .forms import PlayerForm, TrainingForm
from .models import Player, Training, Category


class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['posts'] = Player.objects.all().order_by('-birth_date')
        return context

class AddPlayerView(FormView):
    template_name = "new_player.html"
    form_class = PlayerForm
    success_url = '/'
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        new_object = Player.objects.create(
            jersey_number=form.cleaned_data['jersey_number'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            birth_date=form.cleaned_data['birth_date'],
            email_1=form.cleaned_data['email_1'],
            email_2=form.cleaned_data['email_2'],
        )


        categories = form.cleaned_data['categories']
        new_object.categories.set(categories)
        messages.add_message(self.request, messages.SUCCESS, 'Player added!')
        return super().form_valid(form)

from django.views.generic.edit import FormView
from django.contrib import messages
from .models import Training
from .forms import TrainingForm
from django.urls import reverse
from django.shortcuts import redirect

class AddTraining(FormView):
    template_name = "new_training.html"
    form_class = TrainingForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        # Získaj meno kategórie z URL
        category_name = self.kwargs.get("category_name")
        context = super().get_context_data(**kwargs)
        context['category_name'] = category_name
        return context

    def get_form_kwargs(self):
        # Získať všetky kwargs a pridať category_name
        kwargs = super().get_form_kwargs()
        category_name = self.kwargs.get('category_name')
        kwargs['category_name'] = category_name
        return kwargs

    def form_valid(self, form):
        # Najskôr vytvoríme tréning bez hráčov
        new_training = Training.objects.create(
            category=form.cleaned_data['category'],
            day=form.cleaned_data['day'],
            date=form.cleaned_data['date'],
            time=form.cleaned_data['time'],
        )

        # Priradíme hráčov k tréningu
        all_players_in_category = form.cleaned_data['category'].players.all()
        players = form.cleaned_data['players']
        new_training.players.set(players)

        for player in all_players_in_category:
            player.all_training_count +=1
            player.save()

        # Aktualizujeme attendance_count pre každého hráča
        for player in players:
            player.attendance_count += 1
            player.all_training_count += 1
            player.save()

        messages.success(self.request, "Training added successfully!")
        category_name = form.cleaned_data['category'].name
        return redirect(reverse('dochadzka_app:category', kwargs={'category_name': category_name}))



class CategoryView(TemplateView):
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs.get("category_name")  # Získaj meno kategórie z URL

        selected_category = Category.objects.get(name=category_name)
        players_in_database = selected_category.players.all()
        all_trainings = selected_category.trainings.all()
        counter = 0
        # Inicializuj počítadlo pre každého hráča.
        for player in players_in_database:
            player.attendance_count = 0  # Resetuj počet účastí pre každého hráča
            player.all_training_count = 0
        # Prejdi všetkými tréningami a zisti, ktorí hráči sa zúčastnili
        for training in all_trainings:
            for player in players_in_database:
                player.all_training_count += 1
                if player in training.players.all():
                    player.attendance_count += 1  # Zvýš počet účastí iba pre tohto hráča

        # Pridanie do kontextu
        context["players_in_dorastenci"] = players_in_database
        context["all_trainings"] = all_trainings

        return context


