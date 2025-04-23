from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self,email,username,password):
        if not email:
            raise ValueError("User must have email")
        if not username:
            raise ValueError("User must have username")
        
        user = self.model(email=self.normalize_email(email),username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password):
        if not email:
            raise ValueError("must enter email")
        if not username:
            raise ValueError("must enter username")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField(unique=True,null=True,blank=True)
    username = models.CharField(max_length=50,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True,blank=True)
    phone_number = models.CharField(max_length=11,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def has_perm(self,perms,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True        
    
class Otp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    otp = models.CharField(max_length=4)