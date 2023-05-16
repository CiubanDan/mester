from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
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
                new_user.save()

        return redirect('homepage')


class MemberListView(ListView):
    template_name = 'member/member_list.html'
    model = CustomMember
    context_object_name = 'all_members'

    def get_queryset(self):
        """
        This query returns only members that are NOT workers
        """
        return CustomMember.objects.filter(is_worker=False)

