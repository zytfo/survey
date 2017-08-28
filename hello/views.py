from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect
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
            return HttpResponseRedirect('/en/thanks/')
 
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
            return HttpResponseRedirect('/ru/thanks/')
 
    return render(request, 'survey_ru.html', {
        'form': form}, RequestContext(request))

def results(request):
    if request.user.is_authenticated:
        db = DBAdapter()
        results = db.get_results()
        db.close()
        
        responses = []
        for i in range(len(results['question1'])):
            response = {'id': results['question1'][i][0]}
            q1 = ''
            for j in range(len(results['question1'][i][1:])):
                if results['question1'][i][j + 1]:
                    if not q1 == "":
                        q1 += ", "
                    q1 += SurveyForm.OPTIONS1[j][1]
            response['q1'] = q1
            response['q2'] = results['question2'][i][1]
            response['q3'] = SurveyForm.OPTIONS3[results['question3'][i][1]][1]
            response['q4'] = SurveyForm.OPTIONS4[results['question4'][i][1]][1]
            response['q5'] = results['question5'][i][1]
            responses.append(response)

        # responses = [{'id': 1, 'question1': 'Sports', 'question2': 5}, {'id': 2}, {'id': 3}]

        return render(request, 'results.html', {
	        'results': results, 'responses': responses})
    else:
        return HttpResponseRedirect('/login/')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def auth(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/en/results/')
    else: 
        return HttpResponseRedirect('/login/')

def loginview(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


