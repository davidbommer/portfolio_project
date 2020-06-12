from django.shortcuts import render, get_object_or_404
from .models import Job
# Create your views here.
def home(request):
	return render(request, 'jobs/home.html')

def job_details(request, job_id):
	detail_job = get_object_or_404(Job, pk=job_id)
	if detail_job.title.lower() == 'sudoku':
		return render(request, 'jobs/sudoku.html', {'job':detail_job})
	return render(request, 'jobs/job_details.html', {'job':detail_job})

def job_list(request):
	jobs = Job.objects
	print("got here")
	return render(request, 'jobs/job_list.html', {'jobs':jobs})
