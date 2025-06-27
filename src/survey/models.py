from django.db import models
from django.conf import settings

class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name="Question text")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name="answers")

def __str__(self):
    user_email = self.user.email if self.user else "аноним"
    return f"{self.text} ({user_email})"

class InvalidAnswerAttempt(models.Model):
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.SET_NULL)
    provided_data = models.TextField()
    attempted_at = models.DateTimeField(auto_now_add=True)
