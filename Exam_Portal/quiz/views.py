from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Choice, UserResponse
from django.http import HttpResponseBadRequest
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'quiz/take_quiz.html', {'quiz': quiz, 'questions': questions})

def quiz_result(request, quiz_id):
    if request.method == 'POST':
        user = request.user
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        score = 0
        total_questions = 0
        for question in quiz.question_set.all():
            total_questions += 1
            choice_id = request.POST.get(f'question_{question.id}')
            if choice_id:
                choice = get_object_or_404(Choice, pk=choice_id)
                if choice.is_correct:
                    score += 1
                UserResponse.objects.create(user=user, question=question, choice=choice)
        percentage = (score / total_questions) * 100
        return render(request, 'quiz/quiz_result.html', {'quiz': quiz, 'score': score, 'total_questions': total_questions, 'percentage': percentage})
    else:
        return HttpResponseBadRequest()
