from django.db import models

class subject(models.Model):
    sub_name=models.CharField(max_length=50)
    chapter=models.IntegerField(max_length=50)

    def __str__(self):
        return self.sub_name

class student(models.Model):
    name=models.CharField(max_length=50)
    subject=models.ForeignKey(subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class teacher(models.Model):
    name=models.CharField(max_length=50)
    subject=models.ForeignKey(subject, on_delete=models.CASCADE)

    def __str__(self):
        return 'MR '+str(self.name)+' give '+str(self.subject)

