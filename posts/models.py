from django.db import models
from django.contrib.auth.models import User
# Create your models here.


CATEGORY_TYPE = [
    ('Black Comedy', 'Black Comedy'),
    ('Conditional Joke', 'Conditional Joke'),
    ('Dad Joke', 'Dad Joke'),
    ('Knock-knock', 'Knock-knock'),
    ('Mathematical Joke', 'Mathematical Joke'),
    ('Funny Joke', 'Funny Joke'),
]


class Post(models.Model):
    # title = models.CharField(max_length=50)
    # name = models.CharField(max_length=50)
    content = models.TextField()
    category = models.CharField(choices = CATEGORY_TYPE, max_length = 20) # ekta post multiple categorir moddhe thakte pare abar ekta categorir moddhe multiple post thakte pare
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField()
    share = models.IntegerField()
    # image = models.ImageField(upload_to='posts/media/uploads/', blank = True, null = True)
    def __str__(self):
        return self.category 