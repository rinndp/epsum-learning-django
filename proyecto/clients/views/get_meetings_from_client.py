from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from clients.models import *
from clients.serializers.MeetingSerializer import MeetingSerializer


class GetMeetingsByClientId(APIView):
    def get(self, request, client_id):
        if not ClientModel.objects.filter(id=client_id).exists():
            return Response({
                "error":f"Client not found with id: {client_id}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        meetings = MeetingModel.objects.filter(clients__id=client_id)
        meetings_serializer = MeetingSerializer(meetings, many=True)
        return Response(meetings_serializer.data, status=status.HTTP_200_OK)