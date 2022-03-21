from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm


class SinUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup')
    template_name = 'users/signup.html'


    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user_group = Group.objects.get(name=form.cleaned_data['groups'])
            user.groups.add(user_group)
            # for form_ug in form.cleaned_data['groups']:
            #     user_group = Group.objects.get(name=form_ug)
            #     user.groups.add(user_group)
            return redirect('signup')
        else:
            return render(request, self.template_name, {'form': form})

