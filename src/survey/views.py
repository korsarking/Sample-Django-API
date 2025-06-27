
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema

from .models import Question, Answer
from .serializers import (
    QuestionSerializer,
    AnswerSerializer,
    QuizSummaryItemSerializer,
)


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.filter(is_active=True)
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    http_method_names = ['get', 'post']


@extend_schema(tags=["Quiz"], summary="Get the next question")
class QuizFlowView(APIView):
    def get(self, request):
        next_question = Question.objects.filter(is_active=True).order_by("id").first()
        if next_question:
            serializer = QuestionSerializer(next_question)
            return Response({"question": serializer.data})
        return Response({"message": "Survey completed"})

    @extend_schema(
        tags=["Quiz"],
        summary="Submit answer",
        request=AnswerSerializer
    )
    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = serializer.save()
        return Response({
            "message": "Answer accepted",
            "is_correct": answer.is_correct
        }, status=status.HTTP_201_CREATED)


@extend_schema(tags=["Quiz"], summary="Show quiz results")
class QuizSummaryView(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        correct = answers.filter(is_correct=True).count()
        incorrect = answers.filter(is_correct=False).count()
        serializer = QuizSummaryItemSerializer(answers.order_by("submitted_at"), many=True)

        return Response({
            "total_questions": answers.count(),
            "correct_answers": correct,
            "incorrect_answers": incorrect,
            "accuracy_percent": round((correct / answers.count()) * 100, 1) if answers.exists() else 0.0,
            "completed": True,
            "results": serializer.data
        })


@extend_schema(tags=["Quiz"], summary="Reset all quiz answers")
class QuizResetView(APIView):
    def post(self, request):
        count = Answer.objects.count()
        Answer.objects.all().delete()
        return Response(
            {"message": f"{count} answers deleted. Progress has been reset."},
            status=status.HTTP_200_OK
        )
