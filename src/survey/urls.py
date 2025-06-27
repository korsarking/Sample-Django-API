from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    QuestionViewSet,
    AnswerViewSet,
    QuizFlowView,
    QuizSummaryView,
    QuizResetView
)

router = DefaultRouter()
router.register(r"questions", QuestionViewSet, basename="question")
router.register(r"answers", AnswerViewSet, basename="answer")

urlpatterns = [
    path("api/quiz/", QuizFlowView.as_view(), name="quiz-flow"),
    path("api/quiz/summary/", QuizSummaryView.as_view(), name="quiz-summary"),
    path("api/quiz/reset/", QuizResetView.as_view(), name="quiz-reset"),
]
