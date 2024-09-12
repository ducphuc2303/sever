# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.

# class User(AbstractUser):
#     phone = models.CharField(max_length=100, null=True, blank=True)

#     class Meta(AbstractUser.Meta):
#         swappable = "AUTH_USER_MODEL"
    
#     def __str__(self):
#         return self.username
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=100, null=True, blank=True,)

    # class Meta(AbstractUser.Meta):
    #     swappable = "AUTH_USER_MODEL"
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'auth_user'