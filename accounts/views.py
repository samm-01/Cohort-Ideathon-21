from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import contact
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


def home(request):
    return render(request, 'astra.html')


def signupPage(request):
    if request.method == "POST":
        Full_Name = request.POST.get('Full_Name')
        Email_Id = request.POST.get('Email_Id')
        Batch = request.POST.get('Batch')
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        Contact = contact(Full_Name=Full_Name, Email_Id=Email_Id,
                          Batch=Batch, Username=Username, Password=Password)
        # if exist(Username ==Username):
        #     messages.error(request, "Username Already Taken")
        # if Username is not unique:
        #     messages.error(request, "Username Already Taken")            
        Contact.save()
        messages.success(
            request, "Your Account Has Been Created Successfully.")
        return redirect('signinPage')
    return render(request, 'astra2.html')

# def login(request):
# 	if request.method=='POST':
# 		uname=request.POST.get('username')
# 		passw=request.POST.get('password')

# 		user=authenticate(username=uname,password=passw)
# 		if user:
# 			if user.is_active:
# 				auth_login(request,user)
# 				return HttpResponseRedirect(reverse('homepage'))
# 			else:
# 				return HttpResponse("User is inactive")
# 		else:
# 			messages.info(request, 'Sorry, wrong username or password. Please try again.')
# 			return render(request,'login.html',{'err':'Invalid User Credentia

def signinPage(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['LoginUsername']
        loginpassword = request.POST['LoginPassword']

        Contact = authenticate(username=loginusername, password=loginpassword)
        if Contact is not None:
            login(request, Contact)
            messages.success(request, "Successfully Logged In")
            return redirect("ProjectPage")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("signinPage")

    return render(request, 'astra3.html')

def signoutPage(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def contactusPage(request):
    return render(request, 'astra4.html')


def aboutusPage(request):
    return render(request, 'about.html')


def ProjectPage(request):
    project_list = ProjectInput.objects.all().order_by('-project_date', '-project_time') #kriti
    if request.method == "POST":
        project_name = request.POST.get('project_name') #kriti
        project_date = request.POST.get('project_date') #kriti
        project_time = request.POST.get('project_time')
        project_category = request.POST.get('project_category')
        project_info = request.POST.get('project_info')
        project_image = request.POST.get('project_image')
        projectinput = ProjectInput(project_name = project_name,project_category=project_category,
            project_info=project_info, project_image=project_image, project_date=project_date, project_time=project_time)
        projectinput.save()
        messages.success(
            request, "Your Project Has Been Uploaded Successfully")
        return redirect('ProjectPage')
    return render(request, 'project1.html',
    {'project_list': project_list}) #kriti


def InterviewPage(request):
    interview_list = InterviewInput.objects.all().order_by('-interview_date', '-interview_time')  #kriti
    if request.method == "POST":
        interview_date = request.POST.get('interview_date')#kriti
        interview_time = request.POST.get('interview_time')#kriti
        interview_category = request.POST.get('interview_category')
        interview_info = request.POST.get('interview_info')
        interview_image = request.POST.get('interview_image')
        interviewinput = InterviewInput(
            interview_info=interview_info, interview_category=interview_category, interview_image=interview_image, interview_date=interview_date, interview_time=interview_time)#kriti
        interviewinput.save()
        messages.success(
            request, "Your Interview Experience Has Been Uploaded Successfully")
        return redirect('InterviewPage')
    return render(request, 'interview1.html',{'interview_list': interview_list})#kriti
