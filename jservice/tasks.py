from celery import shared_task

from jservice.logic.services import QuestionLoadService


@shared_task
def load_questions(count: int) -> None:
    question_load_service = QuestionLoadService()
    question_load_service.load(count)
