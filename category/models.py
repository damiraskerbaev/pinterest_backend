from django.db.models import *

class Category(Model):
    name=CharField(
        'Name of the category',
        max_length=100
    )

    image=ImageField(
        'Image of the category',
        upload_to='category-images/'
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'