from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from .models import Greeting
from .forms import SurveyForm, SurveyFormRu, LoginForm
from .dbadapter import DBAdapter
from .localizations import Localization

import os
import psycopg2
import sys

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    first_visit(request)
    if request.session['lang'] == 'en':
        return render(request, 'index.html',
    		{'locale': Localization.strings_en})
    else:
        return render(request, 'index.html',
    		{'locale': Localization.strings_ru})

def thanks(request):
    first_visit(request)
    if request.session['lang'] == 'en':
        return render(request, 'thanks.html',
    		{'locale': Localization.strings_en})
    else:
        return render(request, 'thanks.html',
    		{'locale': Localization.strings_ru})

def survey(request):
    first_visit(request)
    if request.method == 'GET':
        if request.session['lang'] == 'en':
            form = SurveyForm()
        else:
            form = SurveyFormRu()
    else:
        # A POST request: Handle Form Upload
        if request.session['lang'] == 'en':
            form = SurveyForm(request.POST)
        else:
            form = SurveyFormRu(request.POST)
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            if not 'question1' in form.cleaned_data:
                question1 = []
            else:
                question1 = form.cleaned_data['question1']
            question2 = form.cleaned_data['question2']
            question3 = form.cleaned_data['question3']
            question4 = form.cleaned_data['question4']
            question5 = form.cleaned_data['question5']
            if not 'question6' in form.cleaned_data:
                question6 = []
            else:
                question6 = form.cleaned_data['question6']
            db = DBAdapter()
            db.insert_answers(db.get_next_id(), question1, question2, question3, question4, question5, question6)
            db.close()
            return HttpResponseRedirect('/thanks/')
     
    if request.session['lang'] == 'en':
        return render(request, 'survey.html', {
        	'form': form, 'locale': Localization.strings_en}, RequestContext(request))
    else:
        return render(request, 'survey.html', {
        	'form': form, 'locale': Localization.strings_ru}, RequestContext(request))        

def results(request):
    first_visit(request)
    if request.user.is_authenticated:
        db = DBAdapter()
        results = db.get_results()
        db.close()

        if request.session['lang'] == 'en':
            form = Localization.survey_form['en']
            locale = Localization.strings_en
        else:
            form = Localization.survey_form['ru']
            locale = Localization.strings_ru
        form_all = Localization.survey_form['all']
        
        responses = []

        for i in range(len(results['question1'])):
            response = {'id': results['question1'][i][0]}
            q1 = ''
            for j in range(len(results['question1'][i][1:])):
                if results['question1'][i][j + 1]:
                    if not q1 == "":
                        q1 += ", "
                    q1 += form['question_1_choices'][j][1]
            response['q1'] = q1
            response['q2'] = results['question2'][i][1]
            response['q3'] = form['question_3_choices'][results['question3'][i][1]][1]
            response['q4'] = form_all['question_4_choices'][results['question4'][i][1]][1]
            response['q5'] = results['question5'][i][1]
            responses.append(response)

        responses_upd = []
        old_resp = len(results['question1'])
        new_resp = len(results['question6'])
        for i in range(old_resp, old_resp + new_resp):
            response = {'id': results['question6'][i - old_resp][0]}
            q1 = ''
            for j in range(len(results['question6'][i - old_resp][1:])):
                if results['question6'][i - old_resp][j + 1]:
                    if not q1 == "":
                        q1 += ", "
                    q1 += form_all['question_6_choices'][j][1]
            response['q1'] = q1
            response['q2'] = results['question2'][i][1]
            response['q3'] = form['question_3_choices'][results['question3'][i][1]][1]
            response['q4'] = form_all['question_4_choices'][results['question4'][i][1]][1]
            response['q5'] = results['question5'][i][1]
            responses_upd.append(response)

        graphs = {}
        graphs['q1_names'] = [var[1] for var in form['question_1_choices']]
        graphs['q1_values'] = [var[0] for var in results['stat_question1']]

        graphs['q6_names'] = [var[1] for var in form_all['question_6_choices']]
        graphs['q6_values'] = [var[0] for var in results['stat_question6']]

        if not results['stat_question2'][0][0] is None:
            graphs['q2'] = [round(float(results['stat_question2'][0][0]), 2)]
        else:
            graphs['q2'] = 0

        graphs['q3'] = [{'name': form['question_3_choices'][i][1], 'y': results['stat_question3'][i][0]} for i in range(len(form['question_3_choices']))]

        graphs['q4'] = [{'name': form_all['question_4_choices'][i][1], 'y': results['stat_question4'][i][0]} for i in range(len(form_all['question_4_choices']))]

        return render(request, 'results.html', {'responses': responses, 'responses_upd': responses_upd, 'graphs': graphs, 'locale': locale})
    else:
        return HttpResponseRedirect('/login/')

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def login_view(request):
    first_visit(request)
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect('/results/')
    if request.session['lang'] == 'en':
        return render(request, 'registration/login.html', {'form' : form, 'locale': Localization.strings_en})
    else:
        return render(request, 'registration/login.html', {'form' : form, 'locale': Localization.strings_ru})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def changelang(request):
    if request.session['lang'] == 'en':
        request.session['lang'] = 'ru'
        return HttpResponseRedirect(request.GET.get('url'))
    else: 
        request.session['lang'] = 'en'
        return HttpResponseRedirect(request.GET.get('url'))

def first_visit(request):
    if not 'lang' in request.session:
        request.session['lang'] = 'en'


