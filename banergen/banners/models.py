from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=20)


class Banner(models.Model):
    link = models.URLField(max_length=200)
    shows = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, through='BannerCategory')

    def get_absolute_url(self):
        return f'/{self.id}'


class BannerCategory(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
