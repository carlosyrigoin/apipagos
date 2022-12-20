from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from .serializers import ServicesSerializer, Payment_userSerializer, Expired_paymentsSerializer
from .models import Services, Payment_user, Expired_payments

class Expired_paymentsView(APIView):
    #permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        expired_payments = Expired_payments.objects.all().order_by('-id')
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