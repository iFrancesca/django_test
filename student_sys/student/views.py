from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from .models import *
import time
# Create your views here.
from django.shortcuts import render
from .forms import StudentForm

'''
# function view
def index(request):
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
            form = StudentForm()

    context = {
            'students': students,
            'form': form,
        }

    return render(request, 'index.html', context=context)
'''

# class-based view
class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form':form
        })
        return render(request, self.template_name, context)

    def post(self, request):
        context = self.get_context()
        form = StudentForm(self.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context.update({
            'form': form
        })
        return render(request, self.template_name, context)