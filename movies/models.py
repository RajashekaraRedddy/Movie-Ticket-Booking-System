from django.db import models

# Create your models

genres = [
    ['thriller', 'thriller'],
    ['comedy', 'Comedy'],
    ['drama', 'drama'],
    ['romance','romance'],
    ['crime','crime'],
    ['action', 'action'],
    ['animation', 'Animation'],
    ['biography', 'Biography'],
]

languages = [ 
    ['English', 'English'],
    ['Hindi', 'Hindi'],
    ['French', 'French'],
    ['kannada','kannada'],
    ['telugu','telugu'],
    ['tamil','tamil']
    
]

class Movies(models.Model):
    movie_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100,choices=genres)
    language = models.CharField(max_length=100,choices=languages)
    synopsis = models.TextField()
    cast = models.TextField()
    movie_image = models.ImageField(upload_to='movie_images/',null=True,blank=True) 
    duration_minutes = models.IntegerField()
    release_date=models.DateField()
    trailer_url = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=100,null=True,blank=True) 
    slug = models.CharField(max_length=1000,null=True,blank=True)

    def save(self,*args, **kwargs):
        self.slug = self.title.replace(' ','-') 
        super().save(*args,*kwargs) 
      

    def __str__(self):
        return self.title 