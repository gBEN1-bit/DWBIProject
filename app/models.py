"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=158)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class LimitDefinition(models.Model):
    Name = models.CharField(max_length=255, null=True)
    Year = models.IntegerField(null=True)
    Category = models.CharField(max_length=255, null=True)
    Limit = models.CharField(max_length=255, null=True)
    ThresholdTarget = models.CharField(max_length=255, null=True)
    ordernumber = models.BigIntegerField(null=True)
    subCategory = models.CharField(max_length=50, null=True)
    ID = models.AutoField(primary_key=True)
    CategoryCode = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'Limit_Definition_'




        

class CustomerSectorDetails(models.Model):
    CUST_ID = models.CharField(max_length=255)
    LOCATION = models.CharField(max_length=255)
    SECTOR_DESC = models.CharField(max_length=255)
    SECTOR_CODE = models.CharField(max_length=255, null=True)
    OBLIGOR_RISK_RATING = models.FloatField(null=True)
    IFRS_CLASSIFICATION = models.CharField(max_length=255, db_column='IFRS_ CLASSIFICATION')  # Updated column name
    SBU_DIVISION = models.CharField(max_length=255)
    CBK_GRADE = models.FloatField(null=True, db_column='CBK GRADE')


    class Meta:
        db_table = 'stg_customer_sector_details'





