from store.models import NewsArticle
from .models import Blog , Home , Video_HomePage
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import logging

def home(request):
    home= Home.objects.all()
    video = Video_HomePage.objects.first()
    blogs = Blog.objects.all().order_by('-id')[:6]
    latest_news = NewsArticle.objects.filter(is_availble=True).order_by('-publication_date')[:5]  
    context={
        'home': home,
        'main_vidoe': video,
        'latest_news': latest_news ,
        'blogs': blogs
    }
    return render(request, 'home.html', context)

def contact(request):

    return render(request, 'contact.html')

def about(request):

    return render(request, 'about.html')

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
