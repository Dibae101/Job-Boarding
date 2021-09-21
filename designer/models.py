
from django.db import models

from accounts.models import Account

# Create your models here.

DESIGNER_CHOICES = [
    ( 'artist','Artist'),
    ( 'fashion', 'Fashion Designer'),
    ( 'graphics', 'Graphics Designer'),
    ( 'interior', 'Interior Designer'),
    ( 'illustrator', 'Illustrator'),
    ( 'stage', 'Stage Designer'),
    ('ui/ux', 'UX/UI Designer'),
    ( 'web', 'Web Designer'),
    ( 'visual', 'Visual Designer'),
]

class DesignerRegister(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    designer_type = models.CharField(max_length=50, choices=DESIGNER_CHOICES, default = 'Artist')
    bio = models.CharField(max_length=700, blank=True)

    top_skills = models.CharField(max_length=100)

    portfolio_link = models.CharField(max_length=500, blank=True)
    facebook_link = models.CharField(max_length=500, blank=True)
    twitter_link = models.CharField(max_length=500, blank=True)
    linkedin_link = models.CharField(max_length=500, blank=True)
    instagram_link =models.CharField(max_length=500, blank=True)
    
    your_photo = models.ImageField()
    experience = models.CharField(max_length=150)
    tools_of_choice = models.CharField(max_length=100)

    cover_photo = models.ImageField()
    current_status = models.CharField(max_length=150)
    years_of_experience = models.IntegerField()

    resume = models.FileField()
    profile_created = models.BooleanField(default=False)
    
    def __str__(self):
        return self.full_name

class ProjectDescriptionModel(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50, default=None)
    project_link = models.CharField(max_length=150, unique=True, null=True)
    project_description = models.TextField(max_length=200, null=True)
    problem = models.TextField(max_length=1200)
    scope = models.TextField(max_length=1200)
    audience = models.TextField(max_length=1200)
    ideation = models.TextField(max_length=1200)
    competitors = models.TextField(max_length=1200)
    challenges = models.TextField(max_length=1200)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.project_name}'

    

PROTECT_TYPE_CHOICES = [
    ('consumer', 'Consumer'),
    ('B2B', 'B2B'),
    ('design_system','Design System'),
    ('internal_tools', 'Internal Tools'),
]

PLATFORM_CHOICES = [
    ('mobile', 'Mobile'),
    ('responsive_web', 'Responsive Web')
]

PROJECT_STAGE_CHOICES = [
    ( 'concept_idetation', 'Concept and Idetation'),
    ( 'lunched', 'Lunched',),
    ('deprioritized', 'Deprioritized'),
    ('in_progress', 'In Progress'),
]

NUM_COLLABRATE_CHOICES = [
    ('0-1', '0-1 People' ),
    ('1-5', '1-5 People' ),
    ( '6-10', '6-10 People'),
    ( '10+','10+ People'),
]

class ProjectTagsModel(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    project_name = models.OneToOneField(ProjectDescriptionModel, on_delete=models.CASCADE, default=None)
    project_type = models.CharField(max_length=50,choices=PROTECT_TYPE_CHOICES)
    platform_used = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    project_stage = models.CharField(max_length=50, choices=PROJECT_STAGE_CHOICES)
    people_collab_with = models.CharField(max_length=50, choices=NUM_COLLABRATE_CHOICES)

    # def get_url(self):
    #     return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return f'{self.project_name.project_name} - Tags'
    


class DesignerExperience(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    work_title = models.CharField(max_length=100)
    work_location = models.CharField(max_length=150)
    work_description = models.CharField(max_length=1000)
    skills = models.CharField(max_length=150)
    tools_used = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class DesignerEducation(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    education_title = models.CharField(max_length=100)
    location_of_instution = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'