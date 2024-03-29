# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.
# class Quiz(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()

#     def __str__(self):
#         return self.title

# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     text = models.TextField()

#     def __str__(self):
#         return self.text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text = models.CharField(max_length=255)
#     is_correct = models.BooleanField(default=False)

#     def __str__(self):
#         return self.text

# class UserResponse(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user.username}'s response to '{self.question.text}'"

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    choice1 = models.ForeignKey('Choice', on_delete=models.CASCADE, related_name='choice1', null=True, blank=True)
    choice2 = models.ForeignKey('Choice', on_delete=models.CASCADE, related_name='choice2', null=True, blank=True)
    choice3 = models.ForeignKey('Choice', on_delete=models.CASCADE, related_name='choice3', null=True, blank=True)
    choice4 = models.ForeignKey('Choice', on_delete=models.CASCADE, related_name='choice4', null=True, blank=True)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s response to '{self.question.text}'"
