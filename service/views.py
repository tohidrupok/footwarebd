import os
from .models import Publication , Category, Company
import fitz  # PyMuPDF
import tempfile
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render


def publications_list(request):
    publications = Publication.objects.all()

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

    return render(request, 'resource_library.html', {'publications': publications})


def download_pdf(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    pdf_path = os.path.join(settings.MEDIA_ROOT, str(publication.pdf_file))
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(pdf_path)
            return response
    else:
        return HttpResponse("PDF file not found", status=404)
    
    
def supply_chain(request):
    categories = Category.objects.all()
    return render(request, 'supply_chain_info.html', {'categories': categories})
    

def category(request, category_slug=None):

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        companys = Company.objects.filter(title=category)
    print(companys)
    return render(request, 'compnay_list_info.html',  {'companys': companys})