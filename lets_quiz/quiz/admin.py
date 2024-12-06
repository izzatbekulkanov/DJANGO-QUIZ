from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Question, Choice, QuizProfile, AttemptedQuestion
from .forms import QuestionForm, ChoiceForm, ChoiceInlineFormset


class ChoiceInline(admin.TabularInline):
    model = Choice
    can_delete = False
    max_num = Choice.MAX_CHOICES_COUNT
    min_num = Choice.MAX_CHOICES_COUNT
    form = ChoiceForm
    formset = ChoiceInlineFormset


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = (ChoiceInline,)
    list_display = ['html', 'is_published', 'maximum_marks']
    list_filter = ['is_published']
    search_fields = ['html', 'choices__html']
    actions = None
    form = QuestionForm

    def has_delete_permission(self, request, obj=None):
        # Savollarni o'chirishni taqiqlash (faqat misol)
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.pk and obj.is_published:
            return False
        return True


admin.site.register(Question, QuestionAdmin)


class QuizProfileAdmin(admin.ModelAdmin):
    model = QuizProfile
    list_display = ['user', 'total_score']
    search_fields = ['user__username']
    list_filter = ['total_score']


admin.site.register(QuizProfile, QuizProfileAdmin)


class AttemptedQuestionAdmin(admin.ModelAdmin):
    model = AttemptedQuestion
    list_display = ['question', 'quiz_profile', 'selected_choice', 'is_correct', 'marks_obtained']
    search_fields = ['question__html', 'quiz_profile__user__username']
    list_filter = ['is_correct']


admin.site.register(AttemptedQuestion, AttemptedQuestionAdmin)
