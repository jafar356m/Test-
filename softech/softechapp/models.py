from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, name, email, mobile, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            email=self.normalize_email(email),
            mobile=mobile,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, mobile, username, password):
        user = self.create_user(
            name=name,
            email=email,
            mobile=mobile,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email address', unique=True)
    mobile = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile', 'username']

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin 
    
class Post(models.Model):
    Title=models.CharField(max_length=200)
    Descrption=models.CharField(max_length=200)
    Tags=models.CharField(max_length=200)
    date_created=models.DateField(auto_now=True)
    publish=models.BooleanField(default=True)