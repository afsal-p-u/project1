from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from syncdata.permissions import TokenOnlyPermission
from django.db import models
from syncdata.models import AccMaster, ManualCustomer

class CustomerView(APIView):
    permission_classes = [TokenOnlyPermission]

    def get(self, request):
        client_id = request.auth.get("client_id") if request.auth else None

        if not client_id:
            return Response({"error": "Client ID not found in token"}, status=400)

        synced = AccMaster.objects.filter(client_id=client_id).values(
            "code", "name", "phone", "address", "client_id"
        )

        manual = ManualCustomer.objects.filter(client_id=client_id).annotate(
            code=models.F("client_id")
        ).values("code", "name", "phone", "address", "client_id")

        customers = list(synced) + list(manual)
        return Response(customers)

    def post(self, request):
        try:
            if not request.auth:
                return Response({"success": False, "message": "Authentication failed"}, status=401)

            client_id = request.auth.get("client_id")
            if not client_id:
                return Response({"success": False, "message": "Missing client ID"}, status=400)

            data = request.data
            name = data.get("name")
            address = data.get("address", "")
            phone = data.get("phone", "")

            if not name:
                return Response({"success": False, "message": "Name is required."}, status=400)

            if ManualCustomer.objects.filter(client_id=client_id, name=name).exists():
                return Response({"success": False, "message": "Customer already exists."}, status=409)

            ManualCustomer.objects.create(
                client_id=client_id,
                name=name,
                address=address,
                phone=phone
            )

            return Response({"success": True, "message": "Customer added successfully."}, status=201)

        except Exception as e:
            print("❌ Error in POST /customers/:", str(e))
            return Response({"success": False, "message": "Server error"}, status=500)
