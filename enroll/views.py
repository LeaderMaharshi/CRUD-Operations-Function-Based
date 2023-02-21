from django.shortcuts import redirect, render
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            form = StudentRegistration()
            return redirect('addandshow')
    else:
        form = StudentRegistration()
    students = User.objects.all()
        
    context = {
        'form': form,
        'students': students
    }
    return render(request, 'enroll/addandshow.html', context)

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('addandshow')
    
def update_data(request, id):
    if request.method == 'POST':
        student = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:
        student = User.objects.get(pk=id)
        form = StudentRegistration(instance=student)
    context = {
        'form': form,
    }
    return render(request, 'enroll/updatestudent.html', context)