from django.urls import path
from . import views


urlpatterns = [
        path('', views.home, name="home"),
        path('signup/', views.signupPage, name="signupPage"),
		path('signin/', views.signinPage, name="signinPage"),
	    path('signout', views.signoutPage, name="signoutPage"),
		path('contactus/', views.contactusPage, name="contactusPage"),
		path('aboutus/', views.aboutusPage, name="aboutusPage"),
		path('project/', views.ProjectPage, name="ProjectPage"),
		path('interview/', views.InterviewPage, name="InterviewPage"),

]
