# helloworld/views.py
# from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.http import HttpResponseRedirect
# from django.http import HttpResponse
# from django import forms
#
# # Create your views here.
#
#
# class HomePageView(TemplateView):
#
#     def get(self, request, **kwargs):
#         text = """welcome to my Anagram App !"""
#         return render(request, 'index.html', {'text': text})
#
#
# class Home(TemplateView):
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.POST = None
#
#     def get(self, request, *args, **kwargs):
#         context = {'message': 'Hello Django!'}
#         return render(request, "index.html", context=context)
#
#     def get_context_data(request):
#         submitbutton = request.POST.get('Submit')
#         if submitbutton:
#             print("yea")
#         # execute this code
#         context = {'submitbutton': submitbutton}
#         return render(request, 'index.html', context)
#
#     def myview(request):
#         if request.method == "POST":
#             form = MyForm(request.POST)
#             if form.is_valid():
#                 # <process form cleaned data>
#                 return HttpResponseRedirect('/success/')
#         else:
#             form = MyForm(initial={'key': 'value'})
#
#         return render(request, 'post_list.html', {'form': form})
#

from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Person
from django.core.exceptions import *

def index(request):
    return render(request, 'form.html')

def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user = Person.objects.get(name = search_id)
            #do something with user
            html = ("<H1>%s</H1>", user)
            return HttpResponse(html)
        except Person.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'form.html')