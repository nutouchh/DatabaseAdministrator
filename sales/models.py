# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
# class Sales(models.Model):
#     title=models.CharField(max_length=250)
#     author=models.CharField(max_length=250)
#     price=models.FloatField(default=0)
#
#     def __str__(self) -> str:
#         return str(self.title)

class Assortment(models.Model):
    product = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    manufacturer = models.CharField(max_length=250, default='Нет данных')

    def __str__(self) -> str:
        return str(self.product)

    class Meta:
        verbose_name = 'Ассортимент'
        verbose_name_plural = 'Ассортимент'
        ordering = ['product']
        indexes = [models.Index(fields=['product'])]

class Sales(models.Model):
    unit = models.IntegerField()
    rub = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Assortment, on_delete=models.PROTECT)
    region = models.ForeignKey('Geography', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.pk)

    class Meta:
        verbose_name = 'Данные продаж'
        verbose_name_plural = 'Данные продаж'


class Geography(models.Model):
    region = models.CharField(max_length=250)
    federal_district = models.CharField(max_length=250)

    def __str__(self) -> str:
        return str(self.region)

    class Meta:
        verbose_name = 'Географические данные'
        verbose_name_plural = 'Географические данные'
        ordering = ['federal_district', 'region']



# class Purchase(models.Model):
#     PAYMENT_METHODS=[
#     ('Mpesa','Mpesa'),
#     ('Card','Card'),
#     ('Cash','Cash')
#     ]
#     customer=models.CharField(max_length=250)
#     sales=models.ForeignKey('Sales',on_delete=models.CASCADE)
#     payment_method=models.CharField(max_length=6, choices=PAYMENT_METHODS)
#     time_created=models.DateTimeField(auto_now_add=True)
#     is_successful=models.BooleanField(default=True)
#
#     def __str__(self) -> str:
#         return str(self.sales)
