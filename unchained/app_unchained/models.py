from django.db import models
from django import forms

class Question(models.Model):
    text = models.CharField(max_length=200)
       
class QuestionForm(forms.ModelForm):
   class Meta:
     model = Question
     fields = '__all__'

