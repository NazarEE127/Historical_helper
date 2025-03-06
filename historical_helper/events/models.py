from django.db import models


class EventWar(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    participants = models.CharField(max_length=500)
    img_event = models.TextField()

    def __str__(self):
        return f"{self.date}: {self.title}"


class EventCompany(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    img_event = models.TextField()

    def __str__(self):
        return f"{self.date}: {self.title}"


class Chat(models.Model):
    user_question = models.TextField()
    user_id = models.IntegerField()
    date_time = models.DateTimeField()
    ai_answer = models.TextField()

    def __str__(self):
        return f"{self.user_question}: {self.ai_answer}"

