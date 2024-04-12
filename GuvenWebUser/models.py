from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, fullName, phone_number,
                    password=None, is_admin=False, is_cyber_expert=False, is_client=False ):
        if not email:
            raise ValueError('User must Have an email')
        
        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(
            email=self.normalize_email(email),
            fullName=fullName,
            phone_number=phone_number,
            is_admin=is_admin
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        

    def create_superuser(self, email,fullName, phone_number, password=None,is_admin=True, **extra_fields):
        user = self.create_user(
            email=email,
            fullName=fullName,
            phone_number=phone_number, 
            password=password,
            is_admin=is_admin, 
            **extra_fields)

        user.is_admin = True
        user.save(using=self._db)
        return user
    

class GuvenUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    fullName = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_cyber_expert = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName', 'phone_number']

    def get_fullName(self):
        return self.fullName
    
    def check_cyber_expert(self):
        return self.is_cyber_expert
    
    def check_client(self):
        return self.is_client
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

