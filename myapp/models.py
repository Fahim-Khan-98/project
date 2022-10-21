from django.db import models

# Create your models here.
STATE_CHOICE = (
    ('Chittagong','Chittagong'),
    ('Rangpur','Rangpur'),
    ('Rajshahi','Rajshahi'),
    ('Dhaka','Dhaka'),
    ('Jashore','Jashore'),
    ('Dinajpur','Dinajpur'),
    ('Sylhet','Sylhet'),
    ('Pabna ','Pabna '),
    ('Bogra','Bogra'),
    ('Noakhali','Noakhali'),
    ('Faridpur','Faridpur'),
    ('Barisal','Barisal'),
    ('Comilla','Comilla'),
    ('Mymensingh','Mymensingh'),
)
class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateTimeField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE,max_length=100)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profileimg',blank=True)
    my_file = models.FileField(upload_to='doc',blank=True)
