from django.shortcuts import render
from .models import Job
from .forms import ResumeForm

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_portal/job_list.html', {'jobs': jobs})

def submit_resume(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the resume to the job
            job.resumes.create(resume=request.FILES['resume'])
            return render(request, 'job_portal/resume_submitted.html')
    else:
        form = ResumeForm()
    return render(request, 'job_portal/submit_resume.html', {'form': form, 'job': job})
