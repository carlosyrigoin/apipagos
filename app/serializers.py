from rest_framework import serializers
from .models import Services, Payment_user, Expired_payments

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class Payment_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = '__all__'

class Expired_paymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = '__all__'