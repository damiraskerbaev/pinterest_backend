from django.db.models import *
from user.models import User
from category.models import Category

class Post(Model):
    title=CharField(
        'Post of the title',
        max_length=256
    )

    description=TextField(
        'Description of the post',
        blank=True
    )

    created=DateField(
        auto_now_add=True
    )

    image=ImageField(
        'Post of the image',
        upload_to='post-images/'
    )

    user=ForeignKey(
        User,
        on_delete=PROTECT
    )

    watch_count = PositiveBigIntegerField(
        'Views of the post',
        default=0
    )

    like_count=PositiveBigIntegerField(
        'Likes of the post',
        default=0
    )

    category=ForeignKey(
        Category,
        on_delete=PROTECT
    )

    def _str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'