from django.urls import path

from apps.drones.api import api

"""
si es con APIView el view:
from apps.users.api.api import UserAPIView
lo que se pone en el urlpatterns:
path('user/', UserAPIView.as_view(), name='user_api')
"""

urlpatterns = [
    path('drone/', api.drone_api_view, name='drones_api'),
    path('drone/<str:sn>/', api.drone_detail_api_view, name='drones_detail_api'),
    path('check-battery-level/<str:sn>/', api.check_drone_battery, name='drones_check_battery_level'),
    path('availables/', api.drone_available_loading, name='drones_check_availables'),
    path('loading-drone/<str:sn>/', api.loading_drone, name='loading_drone'),
    path('medication/', api.medication_api_view, name='medicationes_api'),
    path('medication/<str:name>/', api.medication_detail_api_view, name='medicationes_detail_api'),

    
]