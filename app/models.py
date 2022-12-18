from django.conf import settings
from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=200)
    descripcion = models.TextField()
    logo = models.URLField(max_length=200)

    def __str__(self):
        return self.name + " - " + self.descripcion

class Payment_user(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    paymentdate = models.DateField(auto_now=True)
    expirationdate = models.DateField()

class expired_payments(models.Model):
    pay_user_id = models.ForeignKey(Payment_user, on_delete = models.CASCADE)
    penalty_free_amount = models.DecimalField(max_digits=18, decimal_places=2)