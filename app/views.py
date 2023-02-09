from app.forms import UserForm
from app.models import User

from http import HTTPStatus

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class IndexView(TemplateView):
    form_class = UserForm()
    template_name = 'index.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['body-class'] = 'design'
        self.context['user_form'] = self.form_class

        return render(request, 'index.html', context=self.context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = UserForm(data=data)

        if form.is_valid():
            form.save()
            if data.get('role') == 'student':
                return HttpResponseRedirect(reverse('students'))
            else:
                return HttpResponseRedirect(reverse('professors'))
        else:
            self.context['user_form'] = form

            return render(request, 'index.html', context=self.context, status=HTTPStatus.NOT_ACCEPTABLE)


class StudentsListView(ListView):
    context_object_name = 'students'
    template_name = 'students_list.html'

    def get_queryset(self):
        queryset = User.objects.filter(role='student').all()

        return queryset


class ProfessorsListView(ListView):
    context_object_name = 'professors'
    template_name = 'professors_list.html'

    def get_queryset(self):
        queryset = User.objects.filter(role='professor').all()

        return queryset


class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_update.html'
    form_class = UserForm
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs

    def get_success_url(self):
        return self.success_url


class UserDeleteView(TemplateView):
    model = User
    template_name = 'index.html'

    def get_object(self, queryset=None):
        object_ = get_object_or_404(self.model, pk=self.kwargs['pk'])
        return object_

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        object.delete()
        return HttpResponseRedirect(reverse('index'))
