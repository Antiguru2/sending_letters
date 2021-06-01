from django.db import models



class Mail_sending(models.Model):
    Mail = models.EmailField(max_length = 30) 
    pub_date = models.DateTimeField("Дата", auto_now_add=True)
    # def __str__(self):
    #     return self.mail
