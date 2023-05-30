from typing import List

from .model import JServiceAPIAdapter, QuestionLoader
from ..models import Question


class QuestionLoadService:
    def load(self, count: int) -> None:
        existing_ids = Question.objects.get_ids()
        question_service = JServiceAPIAdapter()
        loader = QuestionLoader(existing_ids, question_service)
        unique_questions = loader.get_unique_questions(count)
        Question.objects.bulk_create([unique_question.to_db_model() for unique_question in unique_questions])


def get_last_loaded_questions(count: int) -> List[Question]:
    return Question.objects.get_last_loaded(count)
