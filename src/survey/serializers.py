from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "question", "text", "is_correct", "submitted_at"]

    def create(self, validated_data):
        return super().create(validated_data)


class QuizSummaryItemSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source="question.text", read_only=True)
    
    class Meta:
        model = Answer
        fields = ["question_text", "text", "is_correct", "submitted_at"]
