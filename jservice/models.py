from typing import Set

from django.db import models


class QuestionManager(models.Manager):
    def get_last_loaded(self, count: int) -> list:
        query = self.order_by('-loaded_at')[:count]
        return list(query)

    def get_ids(self) -> Set[str]:
        return set(self.values_list('question_id', flat=True))


class Question(models.Model):
    question_id = models.TextField(primary_key=True)
    text = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField()
    loaded_at = models.DateTimeField(auto_now_add=True)

    objects = QuestionManager()

    class Meta:
        db_table = 'questions'
        indexes = [
            models.Index(fields=['-loaded_at'])
        ]
