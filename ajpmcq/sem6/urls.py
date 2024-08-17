from django.urls import path
from . import views

app_name = 'sem6'

urlpatterns = [
    path('', views.display_question, name='question'),
    path('answer/<int:question_id>/', views.display_answer, name='answer'),
]