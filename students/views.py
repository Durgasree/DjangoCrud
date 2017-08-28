from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from students.models import Student


class AllStudents(ListView):
	model = Student

class StudentCreate(CreateView):
	model = Student
	fields = ['name','class_name','phone','address']
	success_url = reverse_lazy('students:all_students')

class StudentUpdate(UpdateView):
	model = Student
	fields = ['name','class_name','phone','address']
	success_url = reverse_lazy('students:all_students')

class StudentDelete(DeleteView):
	model = Student
	success_url = reverse_lazy('students:all_students')