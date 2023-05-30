from __future__ import annotations

import datetime
import time
from dataclasses import dataclass, asdict
from typing import List, Sequence

from .api import JServiceAPI, FetchError
from ..models import Question


@dataclass
class QuestionPrototype:
    question_id: str
    text: str
    answer: str
    created_at: datetime.datetime

    def to_db_model(self) -> Question:
        return Question(**asdict(self))

    @classmethod
    def from_db_model(cls, django_model: Question) -> QuestionPrototype:
        return cls(django_model.question_id, django_model.text, django_model.answer, django_model.created_at)


class JServiceFetchError(Exception):
    pass


class ParseError(Exception):
    pass


class JServiceAPIAdapter:
    def __init__(self):
        self.adaptable = JServiceAPI()

    def get_questions(self, count: int) -> List[QuestionPrototype]:
        try:
            questions = self.adaptable.get_questions(count)
        except FetchError:
            raise JServiceFetchError()
        return [self.question_to_domain(question) for question in questions]

    def question_to_domain(self, question: dict) -> QuestionPrototype:
        try:
            question_id = question['id']
            text = question['question']
            answer = question['answer']
            created_at = question['created_at']
        except KeyError:
            raise ParseError()
        date_format = '%Y-%m-%dT%H:%M:%S.%fZ'
        created_at = datetime.datetime.strptime(created_at, date_format)
        return QuestionPrototype(question_id, text, answer, created_at)


class QuestionLoader:
    def __init__(self, existing_ids: Sequence[str], question_service: JServiceAPIAdapter):
        self.existing_ids = existing_ids
        self.question_service = question_service

    def get_unique_questions(self, count: int) -> List[QuestionPrototype]:
        question_pool = []
        unique_questions = []
        added_ids = set()

        while len(unique_questions) < count:
            if not question_pool:
                try:
                    new_questions = self.question_service.get_questions(count)
                except JServiceFetchError:
                    time.sleep(10)
                    continue
                question_pool.extend(new_questions)
            question = question_pool.pop()
            if question.question_id not in self.existing_ids and question.question_id not in added_ids:
                unique_questions.append(question)
                added_ids.add(question.question_id)
        return unique_questions
