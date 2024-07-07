import os
from .models import Publication , Category, Company, Requirement
import fitz  # PyMuPDF
import tempfile
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render


def publications_list(request):
    publications = Publication.objects.order_by('-id')

    # Iterate through publications and generate URLs for the first page
    for publication in publications:
        pdf_path = publication.pdf_file.path
        try:
            pdf_document = fitz.open(pdf_path)
            first_page = pdf_document.load_page(0)
            image_data = first_page.get_pixmap()
            image_url = '/media/publications/{}_first_page.jpg'.format(publication.id)
            image_path = os.path.join(settings.MEDIA_ROOT, 'publications', '{}_first_page.jpg'.format(publication.id))
            image_data.save(image_path)
            publication.first_page_url = image_url
        except Exception as e:
            print(f"Error processing PDF: {e}")

    return render(request, 'resource/resource_library.html', {'publications': publications})
    
#Supply Chain Info Start  
def supply_chain(request):
    categories = Category.objects.all()
    return render(request, 'chain/supply_chain_info.html', {'categories': categories})
    
def category(request, category_slug=None):

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        companys = Company.objects.filter(title=category)
   
    return render(request, 'chain/compnay_list_info.html',  {'companys': companys})
#Supply Chain Info End

#Certifications and Standards  Start
def certifications_requirement_list(request):
    all_requirement = Requirement.objects.all()

    return render(request, 'certificate/certifications_standards.html', {'requirements': all_requirement})


def requirements_detail(request, requirement_slug):
    requirement = Requirement.objects.get(slug=requirement_slug)

    return render(request, 'certificate/requirement_detail.html', {'requirement': requirement}) 

#Certifications and Standards End