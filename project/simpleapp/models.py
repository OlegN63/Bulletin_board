from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.

class Post(models.Model):
    tanks = 'TK'
    hills = 'HL'
    dd = 'DD'
    traders = 'TR'
    guild_masters = 'GM'
    quest_givers = 'QG'
    blacksmiths = 'BS'
    tanners = 'TN'
    potions_makers = 'PM'
    spell_masters = 'SM'

    CATEGORY = [
        (tanks, 'Танки'),
        (hills, 'Хилы'),
        (dd, 'ДД'),
        (traders, 'Торговцы'),
        (guild_masters, 'Гилдмастеры'),
        (quest_givers, 'Квестгиверы'),
        (blacksmiths, 'Кузнецы'),
        (tanners, 'Кожевники'),
        (potions_makers, 'Зельевары'),
        (spell_masters, 'Мастера заклинаний'),
    ]

    header = models.CharField(max_length=255, default='заголовок')
    body = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORY)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='текст отклика')

    def send_email(self):
        subject = 'Отклик на объявление'
        message = 'Здравствуйте!\n\nНа ваше объявление "{}" появился новый отклик.\n\nС уважением,\nВаш сайт.'.format(
            self.post.header)
        from_email = 'Nikon1987-63rus@yandex.ru'
        recipient_list = [self.post.author.email]

        send_mail(subject, message, from_email, recipient_list)



class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )