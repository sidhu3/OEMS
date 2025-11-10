from django.shortcuts import render,HttpResponse,redirect
from .models import Employee 
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from testapp.forms import SignupForm
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse,reverse_lazy

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'testapp/index.html')


from django.core.paginator import Paginator
@login_required
def all_emp(request):
    emps = Employee.objects.all().order_by('id')
    paginator = Paginator(emps, 10)  # Show 10 employees per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'testapp/view_all_emp.html', {'page_obj': page_obj})

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
        messages.success(request, f"Employee '{first_name} {last_name}' added successfully!")
        return redirect('all_emp')
    elif request.method=='GET':
        return render(request,'testapp/add_emp.html')
    
    else:
        return HttpResponse('An Exception Occurred! Employee has not be added.')
    
@login_required
def remove_emp(request):
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
   
        paginator = Paginator(emps, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'testapp/view_all_emp.html', {'page_obj': page_obj})
    
    elif request.method == 'GET':
        return render(request,'testapp/filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred!')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username.capitalize()}! You’ve logged in successfully.")
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
        
    return render(request, 'testapp/login.html')


def signup_view(request):
    form = SignupForm
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect('/accounts/login/')    
    return render(request,'testapp/signup.html',{'form':form})    

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('/')  

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def custom_password_reset_view(request):
    link = None  # initialize link variable
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            users = User.objects.filter(email=email)
            if users.exists():
                user = users.first()
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                reset_link = request.build_absolute_uri(
                    reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
                )
                link = reset_link  # store the link
    else:
        form = PasswordResetForm()
    
    return render(request, "testapp/forgot_password.html", {"form": form, "reset_link": link})


class UpdateEmployee_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Employee
    fields = ('dept', 'salary', 'bonus', 'role', 'phone')
    success_url = reverse_lazy('all_emp')

    def form_valid(self, form):
        messages.success(self.request, f"Employee '{self.object.first_name} {self.object.last_name}' updated successfully!")
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to update employees.")
        return redirect('all_emp')


class DeleteEmployee(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy('all_emp')
    template_name = 'testapp/employee_confirm_delete.html'

    def post(self, request, *args, **kwargs):
        # get object for message before deletion
        self.object = self.get_object()
        messages.success(request, f"Employee '{self.object.first_name} {self.object.last_name}' deleted successfully!")
        return super().post(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_superuser
      
    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to delete employees.")
        return redirect('all_emp')          