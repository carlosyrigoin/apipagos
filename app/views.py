from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from .serializers import ServicesSerializer, Payment_userSerializer, Expired_paymentsSerializer
from .models import Services, Payment_user, Expired_payments
from django.db.models import F
from .pagination import SimplePagination
import datetime

# Crud Services - ReadOnly

class ServicesView(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Services.objects.all().order_by('-id')
    serializer_class = ServicesSerializer
    pagination_class = SimplePagination


# Crud Payment_user

class Payment_userView(ModelViewSet):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Payment_user.objects.all().order_by('-id')
    pagination_class = SimplePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['paymentdate', 'expirationdate']

    def get_serializer_class(self):
        return Payment_userSerializer

    def list(self, request):
        payments_users = Payment_user.objects.filter(paymentdate__gte = F("expirationdate"))
        for i in payments_users:
            data = {"pay_user_id":i.id, "penalty_free_amount":0}
            serializer = Expired_paymentsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if isinstance(request.data, list):
            serializer = Payment_userSerializer(data=request.data, many = True)
        else:
            serializer = Payment_userSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Payment_user_detailView(ModelViewSet):
    permission_classes = [IsAdminUser]

    def retrieve(self, request, pk=None):
        payment_user = get_object_or_404(self.queryset, pk=pk)
        serializer = Payment_userSerializer(payment_user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        payment_user = get_object_or_404(self.queryset, pk=pk)
        serializer = Payment_userSerializer(payment_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        payment_user = get_object_or_404(self.queryset, pk=pk)
        serializer = Payment_userSerializer(payment_user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        payment_user = get_object_or_404(self.queryset, pk=pk)
        payment_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Crud Expired_payments

class Expired_paymentsView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        expired_payments = Expired_payments.objects.all()
        serializer = Expired_paymentsSerializer(expired_payments, many=True)
        return Response({"ok": True, "data": serializer.data})

    def post(self, request):
        serializer = Expired_paymentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True,  "message": "Created Success"}, status=status.HTTP_201_CREATED)
        return Response({"ok": False, "message": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Expired_payments_detailView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, id):
        expired_payment = get_object_or_404(Expired_payments, pk=id)
        serializer = Expired_paymentsSerializer(expired_payment)
        return Response({"ok": True, "data": serializer.data })

    def put(self, request, id):
        expired_payment = get_object_or_404(Expired_payments, pk=id)
        serializer = Expired_paymentsSerializer(expired_payment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True, "message": "Updated Success"})
        return Response({"ok": False, "message": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        expired_payment = get_object_or_404(Expired_payments, pk=id)
        expired_payment.delete()
        return Response({"ok": True, "message": "Deleted Success"})