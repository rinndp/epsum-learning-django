from datetime import datetime

from django.test import Client
from django.views.generic import CreateView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK
from rest_framework.views import APIView

from clients.models import ClientModel, MeetingModel


def is_valid_datetime(date_string: str):
    try:
        date_format: str = "%Y-%m-%d %H:%M:%S"
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

class CreateMeetingView(APIView):
    def post(self, request):
        purpose = request.data.get('purpose')
        date = request.data.get('date')
        client_id = request.data.get('client_id')

        if not purpose or not date or not client_id:
            return Response({'error': 'Empty fields are not allowed'}, status=HTTP_400_BAD_REQUEST)

        if not is_valid_datetime(date):
            return Response({'error': 'Invalid format date (YYYY-MM-DD HH:MM:SS)'}, status=HTTP_400_BAD_REQUEST)

        if not ClientModel.objects.filter(id=client_id).exists():
            return Response({'error': 'Client does not exist'}, status=HTTP_400_BAD_REQUEST)

        try:
            meeting = MeetingModel.objects.create(
                purpose=purpose,
                date=date,
            )
            client = ClientModel.objects.get(id=client_id)
            meeting.clients.set([client])
            meeting.save()
            return Response({'message': 'Meeting created correctly'}, status=HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"error: {e}"},
                status=HTTP_500_INTERNAL_SERVER_ERROR
            )







