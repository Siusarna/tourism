from django.db import models
from django.utils import timezone

#Модель обратной связи
class Contact(models.Model):
	class Meta():
		db_table = 'contact'
		verbose_name = "Зворотній звязок"
		verbose_name_plural = "Зворотній звязок"

	name = models.CharField("Ім'я та Прізвище", max_length=30)
	email = models.EmailField(max_length=70)
	message = models.TextField("Вкажіть свої побажання на рахунок путівки", max_length=1000)
	data = models.DateTimeField("Дата відправки", default=timezone.now)


	def __str__(self):
		return self.name
