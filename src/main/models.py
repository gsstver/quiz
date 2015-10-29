from jsonfield import JSONField
from django.conf import settings
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name

    @property
    def get_max_weight(self):
        result = 0
        for question in self.questions.all():
            result += question.get_max_weight
        return result


class Question(models.Model):
    test = models.ForeignKey('Test', related_name='questions')
    text = models.TextField()
    order_by = models.PositiveIntegerField(default=10)

    def __str__(self):
        return '{0} / {1}'.format(self.test, self.text)

    @property
    def get_max_weight(self):
        return self.answers.all().aggregate(models.Max('weight'))['weight__max']


class Answer(models.Model):
    question = models.ForeignKey('Question', related_name='answers')
    title = models.CharField(max_length=255)
    weight = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{0} / {1} / {2}'.format(self.question, self.title, self.weight)


class UserTestResult(models.Model):
    test = models.ForeignKey('Test', related_name='results')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='results')
    datetime = models.DateField(auto_now_add=True)
    data = JSONField()

    def __str__(self):
        return '{user} / {time} / {test}'.format(user=self.user, time=self.datetime, test=self.test)

    def get_result_weight(self):
        print(self.data)
        return None
