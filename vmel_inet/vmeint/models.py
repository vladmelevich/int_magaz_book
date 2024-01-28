from django.db import models

class kat(models.Model):
    nm = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.nm



class books(models.Model):
    name = models.CharField(max_length=45)
    im = models.ImageField(upload_to='imag/')
    har = models.TextField()
    price = models.IntegerField()
    kol = models.IntegerField()
    kat = models.ForeignKey(kat, on_delete=models.CASCADE, null=True)
    nam = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'


    def __str__(self):
        return self.name


class za(models.Model):
    nmb = models.IntegerField(null=True)
    user_name = models.CharField(max_length=45,null=True)
    sur_name = models.CharField(max_length=45,null=True)
    kol = models.IntegerField(null=True)
    goro = models.CharField(max_length=45)
    yl = models.CharField(max_length=45)
    adre = models.IntegerField()


    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


    def __str__(self):
        return self.user_name

