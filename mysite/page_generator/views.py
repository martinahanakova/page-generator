from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Participant, Page, PageRating

from .forms import ParticipantCreateForm, PageForm, PageRatingCreateForm


class QuestionaireView(generic.edit.CreateView):
    model = Participant
    form_class = ParticipantCreateForm
    success_url = '/page_generator/page'
    template_name = 'page_generator/questionaire.html'

    def form_valid(self, form):
        object = form.save()
        self.request.session['participant'] = object.id
        form.instance.session_id = self.request.session.session_key
        return super(QuestionaireView, self).form_valid(form)


class PageView(generic.FormView):
    form_class = PageForm
    template_name = 'page_generator/page.html'


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
