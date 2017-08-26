from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .forms import PostForm
from .dbadapter import DBAdapter

import os
import psycopg2

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
def survey(request):
	return render(request, 'survey.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def post_form_upload(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleaned_data['created_at']
            db = DBAdapter()
            db.insert_answers(5, content)
            db.close()
            # post = m.Post.objects.create(content=content,
            #                             created_at=created_at)
            return render(request, 'index.html')
            # return HttpResponseRedirect('/thanks/')
 
    return render(request, 'post_form.html', {
        'form': form,
    })

