from django.contrib import admin
from .models import Question
from .models import Choice


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
	]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
