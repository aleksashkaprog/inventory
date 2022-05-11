from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    code = models.IntegerField(default=1, verbose_name='Код')
    inv = models.CharField(max_length=50, verbose_name='Инвентарный номер')
    price = models.FloatField(verbose_name='Цена')
    count = models.IntegerField(verbose_name='Количество')
    summ = models.FloatField(verbose_name='Сумма')
    note = models.TextField(max_length=100, verbose_name='Примечание')
    resp = models.ForeignKey('Responsible', on_delete=models.CASCADE, related_name='things')

    def __str__(self):
        return self.inv


class Responsible(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')

    def __str__(self):
        return self.name


class General(models.Model):
    product = models.ForeignKey('Thing', on_delete=models.CASCADE, related_name='products')
    people = models.ForeignKey('Responsible', on_delete=models.CASCADE, related_name='peoples')

