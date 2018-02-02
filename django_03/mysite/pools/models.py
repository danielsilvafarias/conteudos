from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	closed = models.BooleanField(default=False)
	pub_date = models.DateTimeField(auto_now_add=True)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=255, default='Teste')
	votes = models.IntegerField(default=0)