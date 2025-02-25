from django.shortcuts import render
from .models import Student

def index(request):
    student_list = Student.objects.all()
    context = {'students': student_list}
    return render(request, 'polls/index.html', context)