from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from .models import Greeting
from .forms import SurveyForm, SurveyFormRu
from .dbadapter import DBAdapter

import os
import psycopg2
import sys

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def thanks(request):
    return render(request, 'thanks.html')

def thanks_ru(request):
    return render(request, 'thanks_ru.html')

def survey(request):
    if request.method == 'GET':
        form = SurveyForm()
    else:
        # A POST request: Handle Form Upload
        form = SurveyForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            question1 = form.cleaned_data['question1']
            question2 = form.cleaned_data['question2']
            question3 = form.cleaned_data['question3']
            question4 = form.cleaned_data['question4']
            question5 = form.cleaned_data['question5']
            db = DBAdapter()
            db.insert_answers(db.get_next_id(), question1, question2, question3, question4, question5)
            db.close()
            # return render(request, 'index.html')
            return HttpResponseRedirect('/thanks/')
 
    return render(request, 'survey.html', {
        'form': form}, RequestContext(request))

def survey_ru(request):
    if request.method == 'GET':
        form = SurveyFormRu()
    else:
        # A POST request: Handle Form Upload
        form = SurveyFormRu(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            question1 = form.cleaned_data['question1']
            question2 = form.cleaned_data['question2']
            question3 = form.cleaned_data['question3']
            question4 = form.cleaned_data['question4']
            question5 = form.cleaned_data['question5']
            db = DBAdapter()
            db.insert_answers(db.get_next_id(), question1, question2, question3, question4, question5)
            db.close()
            # return render(request, 'index.html')
            return HttpResponseRedirect('/thanks_ru/')
 
    return render(request, 'survey_ru.html', {
        'form': form}, RequestContext(request))

def results(request):
    db = DBAdapter()
    results = db.get_results()
    db.close()
 
    return render(request, 'results.html', {
        'results': results})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
