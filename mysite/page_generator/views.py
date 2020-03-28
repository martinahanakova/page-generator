from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Participant, Page, PageRating

from .forms import ParticipantCreateForm, PageRatingCreateForm


class QuestionaireView(generic.edit.CreateView):
    model = Participant
    form_class = ParticipantCreateForm
    success_url = '/page_generator/start_page'
    template_name = 'page_generator/questionaire.html'

    def form_valid(self, form):
        object = form.save()
        self.request.session['participant'] = object.id
        self.request.session['round'] = 1
        form.instance.session_id = self.request.session.session_key
        return super(QuestionaireView, self).form_valid(form)


class StartView(generic.base.TemplateView):
    template_name = 'page_generator/start_page.html'

    def start(request):
        return HttpResponseRedirect('/page_generator/page')


class PageView(generic.ListView):
    model = Page
    template_name = 'page_generator/page.html'

    context_object_name = 'pages'

    def get_queryset(self):
        # get page parameters for actual participant accordind his id and page order
        participant_id = self.request.session['participant']
        order = self.request.session['round']
        pages = Page.objects.filter(participant=participant_id).filter(order=order)

        return pages
class PageRatingView(generic.edit.CreateView):
    model = PageRating
    form_class = PageRatingCreateForm
    success_url = '/page_generator/page'
    template_name = 'page_generator/page_rating.html'

    def form_valid(self, form):
        form.instance.page = self.request.session.participant
        return super(PageRatingView, self).form_valid(form)


class IndexView(generic.ListView):
    template_name = 'page_generator/index.html'
    model = Participant
