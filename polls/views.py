from django.shortcuts import get_object_or_404, render, redirect
from .models import Student, Group
from .forms import StudentRegistrationForm

def student(request):
    student_list = Student.objects.all()
    context = {'students': student_list}
    return render(request, 'polls/student_list.html', context)

def student_detail(request, student_id):
    student_detail = get_object_or_404(Student, pk=student_id)
    context = {'student': student_detail}
    return render(request, 'polls/student_detail.html', context)

def group(request):
    group_list = Group.objects.all()
    context = {'groups': group_list}
    return render(request, 'polls/group_list.html', context)

def group_detail(request, group_id):
    group_detail = get_object_or_404(Group, pk=group_id)
    students = Student.objects.filter(group=group)
    context = {
        'group': group_detail,
        'students': students,
        'headman': students.filter(is_headman=True).first()
    }
    return render(request, 'polls/group_detail.html', context)

def student_registry(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            form = StudentRegistrationForm()
    groups = Group.objects.all()
    context = {'form': form, 'groups': groups}
    return render(request, 'polls/student_registry.html', context)