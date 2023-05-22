from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView
from member.forms import CustomMemberForm
from member.models import CustomMember, Worker


class CustomMemberCreateView(CreateView):
    template_name = 'member/create_member.html'
    model = CustomMember
    form_class = CustomMemberForm

    def form_valid(self, form):
        """
        This validation form checks if new user is a worker, titles his Name
        and commit in the DB
        :return: redirect to HomePage
        """
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            is_worker = form.cleaned_data['is_worker']
            if is_worker:
                new_user.is_worker = True
                new_user.save()
                Worker.objects.create(member=new_user)
            else:
                new_user.is_worker = False
                new_user.save()

        return redirect('homepage')


class WorkerListView(ListView):
    template_name = 'member/worker_list.html'
    model = CustomMember
    context_object_name = 'all_workers'

    def get_queryset(self):
        """
        This query returns only members that are workers
        """
        return CustomMember.objects.filter(is_worker=True)


class MemberListView(ListView):
    template_name = 'member/member_list.html'
    model = CustomMember
    context_object_name = 'all_members'

    def get_queryset(self):
        """
        This query returns only members that are NOT workers
        """
        return CustomMember.objects.filter(is_worker=False)


class MemberDetailView(DetailView):
    template_name = 'member/member_detail.html'
    model = CustomMember


class WorkerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'member/worker_detail.html'
    model = CustomMember

@method_decorator(login_required, name='dispatch')
class AccountDetailView(DetailView):
    model = CustomMember
    template_name = 'member/member_detail.html'
    context_object_name = 'account'

    def get_object(self, queryset=None):
        return self.request.user