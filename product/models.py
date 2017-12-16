from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(verbose_name='标题', max_length=30, blank=False)
    author = models.CharField(verbose_name='发布人', max_length=15, blank=False)
    time = models.DateTimeField(verbose_name='发布时间')
    seenum = models.IntegerField(verbose_name='浏览次数', default=0)
    main = models.TextField(verbose_name="摘要", blank=False, max_length=100)
    content = models.TextField(verbose_name='内容', blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '产品介绍'
        verbose_name_plural = '产品介绍'