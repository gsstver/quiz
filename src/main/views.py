from vanilla import UpdateView, ListView
from django import forms
from django.http import HttpResponseRedirect
from .models import Test, UserTestResult


class PassTestView(UpdateView):
    model = Test
    template_name = 'main/test_pass.html'

    def get_form(self, data=None, files=None, **kwargs):
        cls = self.get_form_class(instance=kwargs['instance'])
        if 'instance' in kwargs:
            del kwargs['instance']
        return cls(data=data, files=files, **kwargs)

    def get_form_class(self, instance):
        fields = {}
        for question in instance.questions.all():
            fields[str(question.pk)] = forms.ChoiceField(
                widget=forms.RadioSelect,
                label=question.text,
                choices=[(answer.weight, answer.title) for answer in question.answers.all()])
        return type('TestPassFormClass', (forms.Form,), fields)

    def form_valid(self, form):
        user_weight = 0
        for key in form.cleaned_data.keys():
            user_weight += int(form.cleaned_data[key])
        self.request.user.results.create(
            test=self.object,
            data={
                'max': self.object.get_max_weight,
                'users': user_weight,
                'data': form.cleaned_data
            }
        )
        return HttpResponseRedirect('/')


class UserTestResultListView(ListView):
    model = UserTestResult

    def get_queryset(self):
        return self.request.user.results.all()
