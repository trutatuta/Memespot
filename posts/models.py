from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class NewPost(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.TextField()
    pub_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def summary(self):
        return self.caption[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
    
