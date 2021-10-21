from django.db import models

# Create your models here.
class signups(models.Model):
    datetime = models.DateTimeField('Время и дата записи')
    user = models.CharField('Имя пользователя', max_length=50)
    wm1 = models.BooleanField('wm1')
    wm2 = models.BooleanField('wm2')
    wm3 = models.BooleanField('wm3')
    wm4 = models.BooleanField('wm4')
    wm5 = models.BooleanField('wm5')
    wm6 = models.BooleanField('wm6')

    def __str__(self):
        return str(self.datetime)
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
