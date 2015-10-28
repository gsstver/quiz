from vanilla import UpdateView
from django import forms
from django.http import HttpResponseRedirect
from .models import Test


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
                choices=[(answer.weight, answer.title) for answer in question.answers.all()])
        return type('TestPassFormClass', (forms.Form,), fields)

    def form_valid(self, form):
        self.request.user.results.create(
            test=self.object,
            data=form.cleaned_data
        )
        return HttpResponseRedirect('/')

