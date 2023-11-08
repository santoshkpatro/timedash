from rest_framework.response import Response
from rest_framework import status, viewsets


class OrderViewSet(viewsets.ViewSet):
    # GET - /api/v1/orders
    def list(self, request):
        return Response(data=[], status=status.HTTP_200_OK)

    # POST - /api/v1/orders
    def create(self, request):
        return Response(data={}, status=status.HTTP_201_CREATED)

    # PATCH - /api/v1/orders/order_b2024eba12a847
    def partial_update(self, request, pk=None):
        return Response(data={}, status=status.HTTP_201_CREATED)
