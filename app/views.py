from app.forms import UserForm
from app.models import User

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.urls import reverse
from django.http import HttpResponseRedirect


class Index(TemplateView):
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
            return render(request, 'index.html', context=self.context)


class StudentsList(ListView):
    context_object_name = 'students'
    template_name = 'students_list.html'

    def get_queryset(self):
        queryset = User.objects.filter(role='student').all()

        return queryset


class ProfessorsList(ListView):
    context_object_name = 'professors'
    template_name = 'professors_list.html'

    def get_queryset(self):
        queryset = User.objects.filter(role='professor').all()

        return queryset
