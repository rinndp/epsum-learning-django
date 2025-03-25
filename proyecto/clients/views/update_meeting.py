from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from clients.models import MeetingModel
from .create_meeting import is_valid_datetime


class UpdateMeetingView(APIView):
    def post(self, request, meeting_id):
        if not request.data['purpose'] or not request.data['date']:
            return Response({
                'error': 'Empty fields are not allowed'},
                status=HTTP_400_BAD_REQUEST
            )

        if not MeetingModel.objects.filter(id=meeting_id).exists():
            return Response({
                "error": f"Meeting not found with id: {meeting_id}"},
                status=HTTP_400_BAD_REQUEST
            )

        if not is_valid_datetime(request.data['date']):
            return Response({'error': 'Invalid format date (YYYY-MM-DD HH:MM:SS)'}, status=HTTP_400_BAD_REQUEST)

        meeting = MeetingModel.objects.get(id=meeting_id)
        meeting.purpose = request.data['purpose']
        meeting.date = request.data['date']
        meeting.save()
        return Response({
            "message": "Meeting updated successfully"},
            status=HTTP_200_OK
        )

