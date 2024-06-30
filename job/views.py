from django.shortcuts import render
from .models import Job
from .forms import ResumeForm

def job_list(request):
    jobs = Job.objects.exclude(title="Post Resume")
    post_resume = Job.objects.filter(title="Post Resume")    # must be add upload resume model's title is:  "Post Resume" use space
    context = {'jobs': jobs , 'post_resume':post_resume }
    return render(request, 'job_portal/job_list.html', context)

def submit_resume(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the resume to the job
             resume_instance = form.save(commit=False)
             resume_instance.job = job  # Associate the resume with the job
             resume_instance.save()
             return render(request, 'job_portal/resume_submitted.html')
    else:
        form = ResumeForm()
    return render(request, 'job_portal/submit_resume.html', {'form': form, 'job': job})  


    # job done for this project
