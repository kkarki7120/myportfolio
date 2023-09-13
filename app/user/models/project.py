from django.db import models

class Project_Message(models.Model):
    id = models.AutoField(primary_key=True,  unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    project = models.CharField(max_length=200)
    budget = models.IntegerField()
    date = models.DateField(auto_now_add=True)



    def project_message_save(self):
        self.save()



    def __str__(self):
        return self.email
    

