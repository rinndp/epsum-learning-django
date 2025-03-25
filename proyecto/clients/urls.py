from django.urls import path, include

from clients.views.create_meeting import CreateMeetingView
from clients.views.get_meetings_from_client import GetMeetingsByClientId
from clients.views.update_meeting import UpdateMeetingView

urlpatterns = [
    path('v1/clients/meetings/<int:client_id>', GetMeetingsByClientId.as_view(), name='get-meetings-by-client-id'),
    path('v1/meetings/create', CreateMeetingView.as_view(), name='create-meeting'),
    path('v1/meetings/update/<int:meeting_id>', UpdateMeetingView.as_view(), name='update-meeting'),
]