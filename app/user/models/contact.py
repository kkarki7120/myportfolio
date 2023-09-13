from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key=True,  unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateField(auto_now_add=True)



    
    def contact_save(self):
        self.save()


    def __str__(self):
        return  self.email
