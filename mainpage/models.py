from enum import unique
from django.db import models

# Create your models here.
class Busan(models.Model):
    id = models.BigAutoField(primary_key=True)
    place = models.CharField(max_length=30)
    lat = models.FloatField()
    lng = models.FloatField()
    subject = models.CharField(max_length=30)
    total = models.IntegerField()
    y2018 = models.IntegerField()
    y2019 = models.IntegerField()
    y2020 = models.IntegerField()
    y2021 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'busan'


class Chungbuk(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungbuk'


class Chungnam(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chungnam'


class Daegu(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daegu'


class Daejeon(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daejeon'



class Gangwon(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangwon'


class Gwangju(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gwangju'


class Gyeongbuk(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongbuk'


class Gyeonggi(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeonggi'


class Gyeongnam(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gyeongnam'


class Incheon(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incheon'


class Jeju(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeju'


class Jeonbuk(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonbuk'


class Jeonnam(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jeonnam'


class Sejong(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sejong'


class Seoul(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seoul'


class Ulsan(models.Model):
    place = models.CharField(primary_key=True, max_length=45)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    y2018 = models.IntegerField(blank=True, null=True)
    y2019 = models.IntegerField(blank=True, null=True)
    y2020 = models.IntegerField(blank=True, null=True)
    y2021 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ulsan'
