from store.models import NewsArticle
from .models import Blog , Home , Video_HomePage, Management_Massage
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import logging

def home(request):
    home= Home.objects.filter(status = True).order_by('-id')
    video = Video_HomePage.objects.first()
    blogs = Blog.objects.all().order_by('-id')[:6]
    latest_news = NewsArticle.objects.filter(is_availble=True).order_by('-publication_date')[:5]  


    form = ContactForm()
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            
            # Send email to admin
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']  # Email provided by the user
            name = form.cleaned_data['name']
            admin_email = settings.DEFAULT_FROM_EMAIL  # Admin email defined in settings
            print(name)
            try:
                send_mail(
                    f"New contact form submission: {subject}",
                    f"Name: {name}\nEmail: {from_email}\n\nMessage:\n{message}",
                    admin_email,  # Sender email, as per settings
                    [admin_email],  # Receiver email, the admin's email
                    fail_silently=False,
                )
               
            except Exception as e:
                logger.error(f"Error sending email: {e}")
                success = False
            
            form = ContactForm()  # Clear the form after successful submission


    context={
        'home': home,
        'main_vidoe': video,
        'latest_news': latest_news ,
        'blogs': blogs ,
        'form': form, 
        'success': success
    }
    return render(request, 'home.html', context) 


def about(request):
    ceo_message = Management_Massage.objects.get(title ="CEO SMS")
    directors_messages = Management_Massage.objects.exclude(title="CEO SMS")
    context = {'ceo_message': ceo_message , 'directors_messages':directors_messages }  

    return render(request, 'about.html', context) 

def choose(request):
    return render(request, 'choose.html') 

def missionvision(request):
    return render(request, 'missionvision.html')  

def management_massage(request):
    ceo_message = Management_Massage.objects.get(title ="CEO SMS")
    directors_messages = Management_Massage.objects.exclude(title="CEO SMS")
    context = {'ceo_message': ceo_message , 'directors_messages':directors_messages } 
    
    return render(request, 'Management_Massage.html', context) 


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs}) 

def blog_detail(request, blog_slug):
    blog = Blog.objects.get(slug=blog_slug)
    return render(request, 'blog_details.html', {'blog': blog})  


# Configure logging
logger = logging.getLogger(__name__)

def contact_view(request):
    form = ContactForm()
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            
            # Send email to admin
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']  # Email provided by the user
            name = form.cleaned_data['name']
            admin_email = settings.DEFAULT_FROM_EMAIL  # Admin email defined in settings

            try:
                send_mail(
                    f"New contact form submission: {subject}",
                    f"Name: {name}\nEmail: {from_email}\n\nMessage:\n{message}",
                    admin_email,  # Sender email, as per settings
                    [admin_email],  # Receiver email, the admin's email
                    fail_silently=False,
                )
               
            except Exception as e:
                logger.error(f"Error sending email: {e}")
                success = False
            
            form = ContactForm()  # Clear the form after successful submission

    return render(request, 'contact_view.html', {'form': form, 'success': success}) 


def logo_animation(request):
    return render(request, 'logo_animation.html')
