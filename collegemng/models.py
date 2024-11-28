from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
# Create your models here.
class TeacherManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Email is not valid")
        email = self.normalize_email(email)
        user  = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email,password,**extra_fields)

class Teacher(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    register_id = models.CharField(max_length=50, unique=True, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = TeacherManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def __str__(self) -> str:
        return self.email

class Student(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,null=True)
    BLOOD_CHOICES = [
        ('A+ve','A+ve'),
        ('A-ve','A-ve'),
        ('B+ve','B+ve'),
        ('B-ve','B-ve'),
        ('AB+ve','AB+ve'),
        ('AB-ve','AB-VE'),
        ('O+ve','O+ve'),
        ('O-ve','O-ve')
    ]
    GENDER_CHOICES = [
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('THIRD GENDER','THIRD GENDER')
        
    ]
    Profile_pic = models.ImageField(upload_to='assest/')
    firstname = models.CharField(max_length=150)
    lastname  = models.CharField(max_length=150)
    register_number = models.CharField(max_length=50,unique=True,null=True, blank=True) 
    email     = models.EmailField(unique=True)
    DoB       = models.DateField()
    Gender    = models.CharField(max_length=50,choices=GENDER_CHOICES)
    Blood_group  = models.CharField(max_length=50,choices=BLOOD_CHOICES)
    Address   = models.TextField()
    City      = models.CharField(max_length=150)
    State     = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.firstname