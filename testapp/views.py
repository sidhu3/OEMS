from django.shortcuts import render,HttpResponse
from .models import Employee,role,Department 
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from testapp.forms import SignupForm
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request,'testapp/index.html')


@login_required
def all_emp(request):
    emps = Employee.objects.all()
    return render(request,'testapp/view_all_emp.html',{'emps':emps})

@login_required
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = float(request.POST['salary'])
        bonus = float(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,dept_id=dept,bonus=bonus,role_id=role,phone=phone,hire_date=datetime.now())
        new_emp.save()
        return all_emp(request)
    elif request.method=='GET':
        return render(request,'testapp/add_emp.html')
    
    else:
        return HttpResponse('An Exception Occurred! Employee has not be added.')
    
@login_required
def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return render(request,'testapp/removed.html')
        
        except:
            return HttpResponse("Please enter a valid emp ID")
    emps = Employee.objects.all()
    return render(request,'testapp/remove_emp.html',{'emps':emps})

@login_required
def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
   
        return render(request,'testapp/view_all_emp.html',{'emps':emps})
    
    elif request.method == 'GET':
        return render(request,'testapp/filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred!')

    return render(request,'testapp/filter_emp.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'testapp/index.html')
    else:
        return render(request,'testapp/logout.html')
    
def signup_view(request):
    form = SignupForm
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password) 
            user.save()
            return HttpResponseRedirect('/accounts/login/')    
    return render(request,'testapp/signup.html',{'form':form})    


class Employee_list_view(ListView):
    model = Employee   

class UpdateEmployee_view(UpdateView):
    model = Employee
    fields = ('dept','salary','bonus','role','phone')

class DeleteEmployee(DeleteView):
    model = Employee
    success_url = reverse_lazy('all_emp')
            