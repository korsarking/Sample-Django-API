from django.contrib import admin
from .models import Question, Answer, InvalidAnswerAttempt

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["text", "created_at", "is_active"]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["text", "question", "is_correct", "submitted_at"]

@admin.register(InvalidAnswerAttempt)
class InvalidAnswerAttemptAdmin(admin.ModelAdmin):
    list_display = ["question", "provided_data", "attempted_at"]

