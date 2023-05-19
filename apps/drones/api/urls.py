from django.urls import path

from apps.drones.api.api import drone_api_view, drone_detail_api_view, medication_api_view, medication_detail_api_view

"""
si es con APIView el view:
from apps.users.api.api import UserAPIView
lo que se pone en el urlpatterns:
path('user/', UserAPIView.as_view(), name='user_api')
"""

urlpatterns = [
    path('drone/', drone_api_view, name='drones_api'),
    path('drone/<str:sn>/', drone_detail_api_view, name='drones_detail_api'),
    path('medication/', medication_api_view, name='medicationes_api'),
    path('medication/<str:name>/', medication_detail_api_view, name='medicationes_detail_api'),

    
]