from rest_framework import views

from api import serializers
from jservice.logic.services import get_last_loaded_questions
from jservice.tasks import load_questions


class LoadAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        load_serializer = serializers.LoadSerializer(data=request.data)
        load_serializer.is_valid(raise_exception=True)
        count = load_serializer.get_count()
        last_loaded_questions = get_last_loaded_questions(count=1)
        load_questions.delay(count)
        question_serializer = serializers.QuestionSerializer(last_loaded_questions, many=True)
        return views.Response({'response': question_serializer.data})
