from django.db import models

# Create your models here.

# class userinfo(models.Model):
#     userID = models.CharField(primary_key, max_length=50)
#     username = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password = models.IntegerField()
#     sex = models.ForeignKey('Online', default=1, on_delete=models.CASCADE, db_constraint=False)
#     birthday

#     class Meta:
#         db_table = "userinfo"



# class student(models.Model):
#         cName = models.CharField(max_length=20, null=False)
#         cSex = models.CharField(max_length=2, default='M', null=False)
#         cBirthday = models.DateField(null=False)
#         cEmail = models.EmailField(max_length=100, blank=True, default='')
#         cPhone = models.CharField(max_length=50, blank=True, default='')
#         cAddr = models.CharField(max_length=255, blank=True, default='')

#         def __str__(self):
#             return self.cName
        
# class studentAdmin(admin.ModelAdmin):
#     list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
#     list_filter=('cName','cSex')
#     search_fields=('cName',)
#     ordering=('id',)