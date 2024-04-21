from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('owner', 'Owner'),
        ('staff', 'Staff'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='staff')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_groups', 
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions', 
        verbose_name='user permissions',
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return f"{self.id}, {self.username}"
    
class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(CustomUser, related_name='shared_files', blank=True)
    assigned_to = models.ManyToManyField(CustomUser, related_name='assigned_files', blank=True)
    parent_folder = models.ForeignKey('Folder', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"File_id : {self.id}, File_name :{self.name}, File_owner: {self.owner}"

class Folder(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parent_folder = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    files = models.ManyToManyField(File, related_name='present_files', blank=True)

    def __str__(self):
        return f"{self.name} : {self.owner}"


