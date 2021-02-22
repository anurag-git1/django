from django.db import models
from .validators import validate_email
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True,validators=[validate_email])
    first_name = models.CharField(max_length=30,help_text="first_name")
    last_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=10,default="") 
    # LOAN_STATUS = (
    #     ('m', 'Maintenance'),
    #     ('o', 'On loan'),
    #     ('a', 'Available'),
    #     ('r', 'Reserved'),
    # )

    # status = models.CharField(
    #     max_length=1,
    #     choices=LOAN_STATUS,
    #     blank=True,
    #     default='m',
    #     help_text='Book availability',
    # ) 

    def __str__(self): 
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        print(self.id)
        #Returns the url to access a particular instance of the model.
        return reverse('user-list', args=[str(self.id)])


class CustomerReportRecord(models.Model):
    time_raised = models.DateTimeField(default=timezone.now, editable=False)
    reference = models.CharField(unique=True, max_length=20)
    description = models.TextField()