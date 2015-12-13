from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse




def paginate(object_list, objects_count, page_num):

    paginator = Paginator(object_list, objects_count)
    try:
        objects_page = paginator.page(page_num)
    except EmptyPage:
            objects_page = paginator.page(paginator.num_pages)
    return objects_page

def index(request, page = 1):
    questions = []
    for i in xrange(1,30):
        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i),
        })
    questions = paginate(questions, 5, page)
    return render(request, 'index.html', {
        'objects': questions,
        'view_name': 'index',
        'url_prefix': '',
    })

def hot_index(request, page = 1):
    questions = []
    for i in xrange(1,10):
        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i),
        })
    questions = paginate(questions, 3, page) 
    return render(request, 'hot.html', {
                'objects': questions,
        'view_name': 'hot_index',
        'url_prefix': '/hot'
        })

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def ask(request):
    return render(request, 'ask.html')

def question(request):
    return render(request, 'question.html')    
    


