from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    from blog.info import department_choice, level_choice, membership_choice

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profile_pic', null=True)
    department = models.CharField(max_length=255, choices=department_choice)
    level = models.CharField(max_length=10, choices=level_choice)
    membership = models.CharField(max_length=20, choices=membership_choice)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def is_representative(self):
        if self.membership == 'representative':
            return True
        return False
            






