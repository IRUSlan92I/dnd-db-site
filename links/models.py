from django.db import models


class Link(models.Model):
    order = models.SmallIntegerField('Order')
    url = models.CharField('URL', max_length=250)
    text = models.CharField('Text', max_length=250)

    def __str__(self):
        return f'({self.order}, {self.url}, {self.text})'
