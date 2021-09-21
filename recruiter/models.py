from django.db import models
from django.db.models.deletion import CASCADE
from django.http import HttpResponse


# Create your models here.

industry = (
    ('accounting', 'Accounting'),
    ('animation', 'Animation'),
    ('apparel and fashion', 'Apparel and Fashion'),
    ('arts and crafts', 'Arts and Crafts'),
    ('aanking', 'Banking'),
    ('computer games', 'Computer Games'),
    ('computer networking', 'Computer Networking'),
    ('cosmetics', 'Cosmetics'),
    ('fine arts', 'Fine Arts'),
    ('financial services', 'Financial Services'),
    ('food and beverages', 'Food and Beverages'),   
    )
size = (
    ('1-10', '1-10'),
    ('11-50', '11-50'),
    ('51-100', '51-100'),
    ('101-250', '101-250'),
    ('251-1000', '251-1000'),
    ('1001-2500', '1001-2500'),
    ('2501+', '2501+'),
    )


class RecruiterRegister(models.Model):
    user = models.OneToOneField("accounts.Account", related_name="recruiter_user", null=True, on_delete=CASCADE)
    image = models.ImageField(upload_to="recruiter/", null=True, blank=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    industry = models.CharField( 
        choices=industry, max_length=100)
    size = models.CharField(
        choices=size, max_length=50)
    company_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name






