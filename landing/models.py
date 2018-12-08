from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        try:
            return 'Пользователь %s %s  %s' %(self.name, self.email, '   ')
        except:
            return "%s" % self.user.id
    class Meta:
        verbose_name = 'My Subscriber'
        verbose_name_plural = 'A lot of Subscribers'


# Create your models here.
