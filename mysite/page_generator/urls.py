from django.urls import path

from . import views


app_name = 'page_generator'
urlpatterns = [
    path('questionaire/', views.QuestionaireView.as_view(), name='questionaire'),
    path('page/', views.PageView.as_view(), name='page'),
    path('page_rating/', views.PageRatingView.as_view(), name='page_rating'),
    path('', views.IndexView.as_view(), name='index'),
]
