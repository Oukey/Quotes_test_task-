from django.db import models


class CryptQuotes(models.Model):
    price = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.time}: {self.price}'
