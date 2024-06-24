from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=status_choices, default=status_choices[0][0])
    planned_date = models.DateField(null=True, blank=True, default="")

    def __str__(self):
        return f"{self.pk}. {self.description}status:{self.status} date:{self.planned_date}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
