from django.db import models

# Create your models here.

class waterConection(models.Model):
    name = models.CharField(max_length=1000, blank = True, null = True)
    wardNo = models.CharField(max_length=10, blank = True, null = True)
    place = models.CharField(max_length=255, blank = True, null = True)
    houseNo = models.CharField(max_length=10, blank = True, null = True)

    def _str_(self):
        return self.name

class regesterComplaintes(models.Model):
    fullName = models.CharField(max_length=1000, blank = True, null = True)
    wardNo = models.CharField(max_length=10, blank = True, null = True)
    place = models.CharField(max_length=255, blank = True, null = True)
    complaintes = models.CharField(max_length=500, blank = True, null = True)
    aboutComplaintes = models.CharField(max_length=1000, blank = True, null = True)

    def _str_(self):
        return self.fullName

class registerUser(models.Model):
    fullName = models.CharField(max_length=1000, blank = True, null = True)
    wardNo = models.CharField(max_length=10, blank = True, null = True)
    houseNo = models.CharField(max_length=10, blank = True, null = True)

    def _str_(self):
        return self.fullName

class waterApplication(models.Model):
    fullName = models.CharField(max_length=1000, blank = True, null = True)
    wardNo = models.CharField(max_length=10, blank = True, null = True)
    place = models.CharField(max_length=255, blank = True, null = True)
    houseNo = models.CharField(max_length=10, blank = True, null = True)

    def _str_(self):
        return self.fullName
