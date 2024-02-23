from django.urls import path
from quiz import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('quiz_list1/', views.quiz_list1, name='quiz_list1'),
    path('quiz_list2/', views.quiz_list2, name='quiz_list2'),
    path('quiz/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
    path('quiz/<int:quiz_id>/result/', views.quiz_result, name='quiz_result'),
]
