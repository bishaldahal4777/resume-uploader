from django.db import models


STATE_CHOICES = (
    ('kathmandu', 'kathmandu'),
    ('Pokhara', 'Pokhara'),
    ('Dolakha', 'Dolakha'),
    ('Bhaktapur', 'Bhaktapur'),
    ('Nepal', 'Nepal'),
    ('Bhaktapur', 'Bhaktapur'),
    ('Gorkha', 'Gorkha'),
    ('Dolpa', 'Dolpa'),
    ('Rolpa', 'Rolpa'),
    ('Jhapa', 'Jhapa'),

)
# Create your models here.
class Resume(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)
