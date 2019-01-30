#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView

# Create your views here.
from django.http import HttpResponse
from django.template import loader

#
def index(request):
    return HttpResponse('Hello World from Polls')
    
#
def book_list(request ):
    print("A")
    return HttpResponse('book_list')
#
def book_test(request ):
#    return HttpResponse('book_test')
#    return render(request, 'book_test.html')
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': Null,
#    }
#    return HttpResponse(template.render(context, request))
    return render(request, 'polls/book_test.html')
#    return render(request, 'polls/index.html')

