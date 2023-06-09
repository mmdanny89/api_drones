from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status      
from apps.drones.api.serializers import DroneSerializer
from apps.drones.models import Drone
from apps.drones.api.serializers import MedicationSerializer
from apps.drones.models import Medication
from django.db.models import Sum


@api_view(['GET', 'POST']) 
def drone_api_view(request):
    
    if request.method == 'GET':
        drones = Drone.objects.all()
        drone_serializer = DroneSerializer(drones, many=True)
        return Response(drone_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        drone_serializer = DroneSerializer(data=request.data)
        if not request.data.get('medicationes') and request.data.get('status') == 'IDLE':
            if drone_serializer.is_valid():
                drone_serializer.save()
                return Response(drone_serializer.data, status=status.HTTP_201_CREATED)
            return Response(drone_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'Drone can by register with IDLE status and empty medicatios case.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def drone_detail_api_view(request, sn=None):

    drone = Drone.objects.filter(serial_number=sn).first()
    if drone:
        if request.method == 'GET':
            drone_serializer = DroneSerializer(drone)
            return Response(drone_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            drone_serializer = DroneSerializer(drone, data=request.data)
            if drone_serializer.is_valid():
                drone_serializer.save()
                return Response(drone_serializer.data, status=status.HTTP_200_OK)
            return Response(drone_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            drone.delete()
            return Response({'message': 'Drone removed successfull.'}, status=status.HTTP_200_OK)
    return Response({'message': "Can't find drone"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST']) 
def medication_api_view(request):
    
    if request.method == 'GET':
        medicationes = Medication.objects.all()
        medication_serializer = MedicationSerializer(medicationes, many=True)
        return Response(medication_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        medication_serializer = MedicationSerializer(data=request.data)
        if medication_serializer.is_valid():
            medication_serializer.save()
            return Response(medication_serializer.data, status=status.HTTP_201_CREATED)
        return Response(medication_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def medication_detail_api_view(request, code=None):

    medication = Medication.objects.filter(code=code).first()
    if medication:
        if request.method == 'GET':
            medication_serializer = MedicationSerializer(medication)
            return Response(medication_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            medication_serializer = MedicationSerializer(medication, data=request.data)
            if medication_serializer.is_valid():
                medication_serializer.save()
                return Response(medication_serializer.data, status=status.HTTP_200_OK)
            return Response(medication_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            medication.delete()
            return Response({'message': 'Medication removed successfull.'}, status=status.HTTP_200_OK)
    return Response({'message': "Can't find Medication"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def check_drone_battery(request, sn=None):
    drone = Drone.objects.filter(serial_number=sn).first()
    if drone:
        return Response({'battery': drone.get_battery_capacity()}, status=status.HTTP_200_OK)
    return Response({'message': "Can't find Drone."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def drone_available_loading(request):
    drones = Drone.objects.filter(status='IDLE')
    if drones:
        return Response({'drones': [d.__str__() for d in drones]}, status=status.HTTP_200_OK)
    return Response({'message': "Not availables Drones"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def loading_drone(request, sn=None):
    medications_code = request.data.get('medications')
    drone = Drone.objects.filter(serial_number=sn).first()
    if drone:
        if drone.battery_capacity >= 25:
            if Medication.objects.filter(code__in=medications_code):
                if Medication.objects.filter(code__in=medications_code).aggregate(Sum('weight'))['weight__sum'] <= drone.weight_limit:
                    drone.status = 'LOADING'
                    drone.save()
                    for m in Medication.objects.filter(code__in=medications_code):
                        drone.medicationes.add(m)
                    drone.status = 'LOADED'
                    drone.save()
                    d_ser = DroneSerializer(drone)
                    return Response(d_ser.data, status=status.HTTP_200_OK)
                return Response({'message': "Drone overweight."}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': "Invalid Medications code."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': "Drone low battery."}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': "Can't find Drone."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def check_loaded_medication_drone(request, sn=None):
    drone = Drone.objects.filter(serial_number=sn).first()
    if drone:
        medications = drone.medicationes.all()
        if medications:
            medi = [MedicationSerializer(m).data for m in drone.medicationes.all()]
            return Response({"medications": medi}, status=status.HTTP_200_OK)
        return Response({"medications": []}, status=status.HTTP_200_OK)
    return Response({'message': "Can't find Drone."}, status=status.HTTP_404_NOT_FOUND)