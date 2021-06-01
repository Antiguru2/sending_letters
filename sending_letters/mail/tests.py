
from django.test import TestCase
from django.test import Client
# from django.views.decorators import cache
from .models import Mail_sending
from django.core import mail



class Mail_sending_test(TestCase):
    def setUp(self):
        # create Client
        self.client = Client()
        # create Mail_sending
        self.mail = "test@yandex.ru"
        self.text = "test"
        self.int = 1

    def test_mail_sending(self):
        # формируем GET-запрос к странице сайта
        response = self.client.get(f"/sendemail/")
        self.assertEqual(response.status_code, 404)

        response = self.client.post(f"/sendemail/", { 'Mail': self.mail })
        # проверка на создание модели в бд, отправления почты, передачи мейла из post в адрес направления поста    
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [self.mail])
        self.assertEqual(len(Mail_sending.objects.all()), 1)
        # если в посте придет str
        response = self.client.post(f"/sendemail/", { 'Mail': self.text })
        self.assertEqual(response.status_code, 404)
        # если в посте придет int
        response = self.client.post(f"/sendemail/", { 'Mail': self.int })
        self.assertEqual(response.status_code, 404)
