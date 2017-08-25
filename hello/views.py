from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

from .forms import PostForm

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
            conn = psycopg2.connect(
                database="dcrer4f7hatr58",
                user="wngxswjyulxtwx",
                password="2b09bd90d6261888f0415ca2b3ae8eb11df089812f5354934e4ca696d31036c2",
                host="ec2-79-125-13-42.eu-west-1.compute.amazonaws.com",
                port="5432"
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO question_5(survey_id, text) VALUES('rabotai', ?)")
            conn.close()
            # post = m.Post.objects.create(content=content,
            #                             created_at=created_at)
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id': 4}))
 
    return render(request, 'post_form.html', {
        'form': form,
    })

