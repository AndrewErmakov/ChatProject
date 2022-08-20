from django.contrib.auth import get_user_model
from django.db.models import Model, ForeignKey, CASCADE, TextField, DateTimeField

User = get_user_model()


class Message(Model):
    author = ForeignKey(to=User, on_delete=CASCADE, related_name='messages')
    content = TextField()
    created_ad = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    @staticmethod
    def last_messages():
        return Message.objects.all().order_by('-created_ad')[:10]
