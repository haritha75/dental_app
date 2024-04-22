from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request) :
  return render(request,'home.html',{})
def about(request) :
  return render(request,'about.html',{})
def service(request) :
  return render(request,'service.html',{})
def price(request) :
  return render(request,'pricing.html',{})
def blog(request) :
  return render(request,'blog.html',{})
def blog_details(request) :
  return render(request,"blog-details.html",{})

def contact(request) :
  if request.method == "POST":

    message_name = request.POST['message-name']
    message_email =request.POST['message-email']
    message=request.POST['message']

    # send mail
    send_mail(
      message_name, #subject
      message, #message
      message_email,#from
      ['yerukonduhatiha@gmail.com'],#to
      fail_silently=False, # to display error on the console make false
    )
    return render(request,'contact.html',{'message_name':message_name})
  
  else:

    return render(request,'contact.html',{})