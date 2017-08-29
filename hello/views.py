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
from .localizations import Localization

import os
import psycopg2
import sys

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html', {'locale': Localization.strings_en})

def thanks(request, locale):
    if locale == 'en':
        return render(request, 'thanks.html',
    		{'locale': Localization.strings_en})
    else:
        return render(request, 'thanks.html',
    		{'locale': Localization.strings_ru})

def survey(request, locale):
    if request.method == 'GET':
        if locale == 'en':
            form = SurveyForm()
        else:
            form = SurveyFormRu()
    else:
        # A POST request: Handle Form Upload
        if locale == 'en':
            form = SurveyForm(request.POST)
        else:
            form = SurveyFormRu(request.POST)
 
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
            if locale == 'en':
                return HttpResponseRedirect('/en/thanks/')
            else:
                return HttpResponseRedirect('/ru/thanks/')
     
    if locale == 'en':
        return render(request, 'survey.html', {
        	'form': form, 'locale': Localization.strings_en}, RequestContext(request))
    else:
        return render(request, 'survey.html', {
        	'form': form, 'locale': Localization.strings_ru}, RequestContext(request))        

def results(request, locale):
    if request.user.is_authenticated:
        db = DBAdapter()
        results = db.get_results()
        db.close()

        if locale == 'en':
            form = SurveyForm()
        else:
            form = SurveyFormRu()
        
        responses = []
        for i in range(len(results['question1'])):
            response = {'id': results['question1'][i][0]}
            q1 = ''
            for j in range(len(results['question1'][i][1:])):
                if results['question1'][i][j + 1]:
                    if not q1 == "":
                        q1 += ", "
                    q1 += form.OPTIONS1[j][1]
            response['q1'] = q1
            response['q2'] = results['question2'][i][1]
            response['q3'] = form.OPTIONS3[results['question3'][i][1]][1]
            response['q4'] = form.OPTIONS4[results['question4'][i][1]][1]
            response['q5'] = results['question5'][i][1]
            responses.append(response)

        if locale == 'en':
            return render(request, 'results.html', {
        		'results': results, 'responses': responses, 'locale': Localization.strings_en})
        else:
            return render(request, 'results.html', {
        		'results': results, 'responses': responses, 'locale': Localization.strings_ru})
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


