from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from job.forms import JobCreateForm
from job.models import Job, Contract
from member.models import CustomMember, Worker


class JobCreateView(LoginRequiredMixin, CreateView):
    template_name = 'job/create_job.html'
    model = Job
    form_class = JobCreateForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        """
        This function get Email from the user that post the job
        :param form:
        :return:
        """
        custom_member = CustomMember.objects.get(email=self.request.user.email)
        form.instance.member = custom_member
        return super().form_valid(form)


class JobListView(LoginRequiredMixin, ListView):
    template_name = "job/list_jobs.html"
    model = Job
    context_object_name = 'all_jobs'



class JobDetailView(LoginRequiredMixin, DetailView):
    template_name = "job/job_details.html"
    model = Job

    def post(self, request, *args, **kwargs):
        """
        This function verify if the account is worker ,
        and save in Contract model the status!
        """
        job = self.get_object()
        worker = get_object_or_404(Worker, member__email=request.user.email)

        if worker and worker.worker_category == job.category_type:
            job.status = 'In Progress'
            job.save()
            contract = Contract(worker=worker, job=job)
            contract.save()
            return redirect('detail-job', pk=job.pk)

        else:

            return render(request, 'job/not_worker.html')


    # def get_context_data(self, **kwargs):
    #
    #     data = super().get_context_data(**kwargs)
    #     worker_data = self.get_object()
    #     worker = worker_data.worker.first()
    #     if worker_data:
    #         data['worker_data'] = worker
    #     return data

class JobDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'job/delete_job.html'
    model = Job

