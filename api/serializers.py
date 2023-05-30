from rest_framework import serializers

from jservice.models import Question


class LoadSerializer(serializers.Serializer):
    questions_num = serializers.IntegerField()

    def get_count(self) -> int:
        return self.validated_data.get('questions_num')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_id', 'text', 'answer', 'created_at')
