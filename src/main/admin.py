from django.contrib import admin
from .models import Test, Question, Answer, UserTestResult


class QuestionInline(admin.TabularInline):
    model = Question


class AnswerInline(admin.TabularInline):
    model = Answer


class TestAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline
    ]


admin.site.register(Test, TestAdmin)

admin.site.register(Question, QuestionAdmin)

admin.site.register(Answer)

admin.site.register(UserTestResult)

