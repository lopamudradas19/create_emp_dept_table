from django.db import models

# Create your models here.
class dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name
    


class emp(models.Model):
    emp_no=models.IntegerField()
    ename=models.CharField(max_length=100)
    dept_no=models.ForeignKey(dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename