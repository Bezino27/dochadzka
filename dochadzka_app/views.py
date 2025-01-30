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
        messages.add_message(self.request, messages.SUCCESS, 'Player added!')
        return super().form_valid(form)

from django.views.generic.edit import FormView
from django.contrib import messages
from .models import Training
from .forms import TrainingForm

class AddTraining(FormView):
    template_name = "new_training.html"
    form_class = TrainingForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Najskôr vytvoríme tréning bez hráčov
        new_training = Training.objects.create(
            category=form.cleaned_data['category'],
            day=form.cleaned_data['day'],
            date=form.cleaned_data['date'],
            time=form.cleaned_data['time'],
        )

        player = form.cleaned_data['player']
        new_training.player.set(player)

        for hrac in player:
            hrac.attendance_count += 1
            hrac.save()

        messages.add_message(self.request, messages.SUCCESS, 'Training added!')
        return super().form_valid(form)


class CategoryView(TemplateView):
    template_name = "category.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories= Category.objects.all()


        # Získaj hodnotu z GET požiadavky pre filtrovanie
        input_category_name = self.request.GET.get('category_input')

        if input_category_name:
            # Filtrovanie podľa názvu kategórie
            context['categories'] = categories
            context['value'] = input_category_name  # Tento parameter pošleme do šablóny
        else:
            # Ak nebola vybraná kategória, zobrazíme všetky kategórie
            context['categories'] = categories
            context['value'] = None  # Ak neexistuje výber kategórie, neukážeme nič špecifické

        return context