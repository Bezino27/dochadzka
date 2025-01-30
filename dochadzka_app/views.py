from django.contrib import messages
from django.views.generic import TemplateView, FormView

from .forms import PlayerForm
from .models import Player

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