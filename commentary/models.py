from django.db.models import *

from user.models import User
from post.models import Post

class Commentary(Model):
    user=ForeignKey(
        User,
        on_delete=PROTECT
    )

    post=ForeignKey(
        Post,
        on_delete=PROTECT
    )

    commentary=CharField(
        'Commentary of the post',
        max_length=1000
    )

    def __str__(self):
        return f'{self.commentary}'

    class Meta:
        verbose_name='Commentary'
        verbose_name_plural='Commentaries'