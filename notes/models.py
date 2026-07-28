from django.db import models


class MongoNote(models.Model):
    """Admin-only proxy model. Records are stored in MongoDB, not SQL."""

    student_id = models.CharField(max_length=20)
    note = models.TextField()

    class Meta:
        managed = False
        verbose_name = 'Student Note (MongoDB)'
        verbose_name_plural = 'Student Notes (MongoDB)'

    def __str__(self):
        return f'{self.student_id}: {self.note[:50]}'
