from django.urls import reverse_lazy
from django.views import generic
from school.models import DayOfTheWeek
from school.models import Classroom
from school.models import Course
from django.http import  JsonResponse

__all__ = ['DayOfTheWeekListView']

class DayOfTheWeekListView(generic.ListView):
    model = DayOfTheWeek

class DayOfTheWeekDetailView(generic.DetailView):
    model = DayOfTheWeek

class classroomListView(generic.ListView):
    model = Classroom

class classroomDetailView(generic.DetailView):
    model = Classroom

class courseListView(generic.ListView):
    model = Course

class courseDetailView(generic.DetailView):
    model = Course

class DayOfTheWeekCreateView(generic.CreateView):
    model = DayOfTheWeek
    fields = ['number', 'name']
    def get_success_url(self):
        return reverse_lazy('dayoftheweek_detail', kwargs={'pk': self.object.pk})

class DayOfTheWeekUpdateView(generic.UpdateView):
    model = DayOfTheWeek
    fields = ['number', 'name']
    def get_success_url(self):
        return reverse_lazy('dayoftheweek_detail', kwargs={'pk': self.object.pk})

class DayOfTheWeekDeleteView(generic.DeleteView):
    model = DayOfTheWeek
    success_url = reverse_lazy('dayoftheweek_list')

class classroomCreateView(generic.CreateView):
    model = Classroom
    fields = ['name', 'capacity']
    def get_success_url(self):
        return reverse_lazy('classroom_detail', kwargs={'pk': self.object.pk})

class classroomUpdateView(generic.UpdateView):
    model = Classroom
    fields = ['name', 'capacity']
    def get_success_url(self):
        return reverse_lazy('classroom_detail', kwargs={'pk': self.object.pk})

class classroomDeleteView(generic.DeleteView):
    model = Classroom
    success_url = reverse_lazy('classroom_list')

class courseCreateView(generic.CreateView):
    model = Course
    fields = ['subject', 'starting_hour', 'day_of_the_week', 'classroom', 'school']
    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.pk})

class courseUpdateView(generic.UpdateView):
    model = Course
    fields = ['subject', 'starting_hour', 'day_of_the_week', 'classroom', 'school']
    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.pk})

class courseDeleteView(generic.DeleteView):
    model = Course
    success_url = reverse_lazy('course_list')


def api_example(request):
    data = {"prova": "hello world!"}
    return JsonResponse(data)