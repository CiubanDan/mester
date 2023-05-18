from django.urls import reverse_lazy
from django.views.generic import CreateView
from job.forms import JobCreateForm
from job.models import Job


class JobCreateView(CreateView):
    template_name = 'job/create_job.html'
    model = Job
    form_class = JobCreateForm
    success_url = reverse_lazy('homepage')


