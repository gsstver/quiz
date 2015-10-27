from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    test = models.ForeignKey('Test', related_name='questions')
    text = models.TextField()
    order_by = models.PositiveIntegerField(default=10)

    def __str__(self):
        return '{0} / {1}'.format(self.test, self.text)


class Answer(models.Model):
    question = models.ForeignKey('Question', related_name='answers')
    title = models.CharField(max_length=255)
    weight = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{0} / {1} / {2}'.format(self.question, self.title, self.weight)
