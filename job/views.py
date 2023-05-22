from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from job.forms import JobCreateForm
from job.models import Job
from member.models import CustomMember


class JobCreateView(CreateView):
    template_name = 'job/create_job.html'
    model = Job
    form_class = JobCreateForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        custom_member = CustomMember.objects.get(email=self.request.user.email)
        form.instance.member = custom_member
        return super().form_valid(form)

