from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class LectureListView(ListView):
    model = Lecture
    template_name = 'lecture_list.html'

class LectureDetailView(DetailView):
    model = Lecture
    template_name = 'lecture_detail.html'

class LectureCreateView(CreateView):
    model = Lecture
    template_name = 'lecture_form.html'
    fields = ['title', 'description']

class LectureUpdateView(UpdateView):
    model = Lecture
    template_name = 'lecture_form.html'
    fields = ['title', 'description']

class LectureDeleteView(DeleteView):
    model = Lecture
    template_name = 'lecture_confirm_delete.html'
    success_url = reverse_lazy('lecture-list')
