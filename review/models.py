from django.db import models
from django.db.models.enums import Choices

class Post(models.Model):

    RATING_CHHOICES = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),       
        ('10','10'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField(null= True)
    rating = models.CharField(max_length=6, choices=RATING_CHHOICES, default='5')



# Create your models here.
