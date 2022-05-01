from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Question,QuestionForm
from django.shortcuts import render

def band_create(request):
   form = QuestionForm()
   return render(request,
            'app_unchained/create.html',
            {'form': form})

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions,}
    return render(request, 'app_unchained/index.html', context)

def create_index(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = QuestionForm()
    return render(request,
            'app_unchained/create.html',
            {'form': form})

def delete_view(request, id):
    obj = get_object_or_404(Question, id = id)
    obj.delete()
    return HttpResponseRedirect("/")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'app_unchained/detail.html', {'question': question})

def update_view(request, id):
    context ={}
    obj = get_object_or_404(Question, id = id)
    form = QuestionForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form
 
    return render(request, "app_unchained/update.html", context)

def chat(request):
    return render(request, 'app_unchained/chat.html')

def room(request, room_name):
    return render(request, 'app_unchained/room.html', {
        'room_name': room_name
    })