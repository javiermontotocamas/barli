from django.shortcuts import HttpResponse
from django.http import JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import TableSerializer, UserProfileSerializer, BarSerializer, AdvertisementSerializer
from .models import *



#ZONA REGISTRO
class RegisterView(APIView):
    def post(self, request, format=None):
        user_type = request.data["type"]
        record_data = request.data["recordData"]
        serializer = None
        if user_type == "customer":
            serializer = UserProfileSerializer(data=record_data)
        elif user_type == "bar":
            serializer = BarSerializer(data=record_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Vista protegida
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_number_list(request):
    """
    A simple private view that requires JWT authentication.
    """
    numbers = [1, 2, 3, 4, 5]
    response_data = {'numbers': numbers}
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated]) # TODO: Ver como hacer una validacion para que sea el bar sea el mismo que me esta pidiendo los datos
def get_tables_of_bar(request, id):
    tables = Bar.objects.get(pk=id).table_set.all()
    serializer = TableSerializer(data=tables, many=True)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated]) # TODO: Ver como hacer una validacion para que sea el bar sea el mismo que me esta pidiendo los datos
def process_ads_of_bar(request, id):
    if request.method == "GET":
        ads = Bar.objects.get(pk=id).advertisement_set.all()
        serializer = AdvertisementSerializer(data=ads, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        bar = Bar.objects.get(pk=id)
        serializer = AdvertisementSerializer(data={'bar': bar.id, 'product_name': request.data["product_name"], 'reduction': request.data['reduction']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(None, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated]) # TODO: Ver como hacer una validacion para que sea el bar sea el mismo dueño que quiere borrar el anuncio
def delete_ad_of_bar(request, bar_id, ad_id):
    # bar_id de momento no lo utilizo, lo utlilizaria mas adelante para verificar la validacion de que sea el bar correspondiente...
    # primero deberia verificar que el ad_id es dichero bar_id
    # que el bar_id es el mismo que tengo en el token
    ad = Advertisement.objects.get(pk=ad_id)
    ad.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)


#ZONA INFO CUENTA BAR
@api_view(['GET','PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated]) # TODO: Ver como hacer una validacion url
def process_data_of_bar(request, id):
    if request.method == "GET":
        bar_info = Bar.objects.get(pk=id)
        serializer = BarSerializer(bar_info)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        bar_info = Bar.objects.get(pk=id)
        serializer = BarSerializer(data={'id': request.user.id, 'user': request.data['username'], 'name': request.data['recordData']['name'], 'description': request.data['recordData']["description"], 'phone': request.data['recordData']['phone'], 'address': request.data['recordData']['address'], 'latitude': request.data['recordData']['latitude'], 'longitude': request.data['recordData']['longitude']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(None, status=status.HTTP_405_METHOD_NOT_ALLOWED)




def index(request):
    return HttpResponse('Bienvenido a la api')   

#Obtener todos los usuarios
def get_users(request):
    # Recupera todos los perfiles de usuario
    profiles = UserProfile.objects.all()

    # Convierte los datos en una lista de diccionarios
    profile_data = [{
                'id': profile.id,
                'fullname': profile.fullname,
                'phone': profile.phone,
                'email': profile.email,
                'birthdate': profile.birthdate,
                } for profile in profiles]

    return JsonResponse({'user_profiles': profile_data}, safe=False)

#Obtener usuario por id
def get_user_by_id(request, user_id):
    try:
        profile = UserProfile.objects.get(id=user_id)
        profile_data = {
            'id': profile.id,
            'fullname': profile.fullname,
            'phone': profile.phone,
            'email': profile.email,
            'birthdate': profile.birthdate
        }
        return JsonResponse({'user_profile': profile_data})
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'Perfil de usuario no encontrado'}, status=404)
    

#Obtener todos los bares
def get_bars(request):
    profiles = Bar.objects.all()

    profile_data = [{
                'id': profile.id,
                'name': profile.name,
                'description': profile.description,
                'phone': profile.phone,
                'email': profile.email,
                'adress': profile.address,
                'latitude': profile.latitude,
                'longitude': profile.longitude
                } for profile in profiles]

    return JsonResponse({'bar_profiles': profile_data}, safe=False)

#Obtener bar por id
def get_bar_by_id(request, bar_id):
    try:
        profile = Bar.objects.get(id=bar_id)
        profile_data = {
            'id': profile.id,
            'name': profile.name,
            'description': profile.description,
            'phone': profile.phone,
            'email': profile.email,
            'adress': profile.address,
            'latitude': profile.latitude,
            'longitude': profile.longitude
        }
        return JsonResponse({'bar_profile': profile_data})
    except Bar.DoesNotExist:
        return JsonResponse({'error': 'Bar no encontrado'}, status=404)
    

#Obtener todas las promociones
def get_ad(request):
    profiles = Advertisement.objects.all()

    profile_data = [{
                'id': profile.id,
                'bar': profile.bar,
                'product_name': profile.product_name,
                'reduction': profile.reduction
                } for profile in profiles]

    return JsonResponse({'advertisements': profile_data}, safe=False)

#Obtener promocion por id
def get_ad_by_id(request, ad_id):
    try:
        profile = Advertisement.objects.get(id=ad_id)
        profile_data = {
            'id': profile.id,
            'bar': profile.bar,
            'product_name': profile.product_name,
            'reduction': profile.reduction
        }
        return JsonResponse({'advertisement': profile_data})
    except Advertisement.DoesNotExist:
        return JsonResponse({'error': 'Promocion no encontrada'}, status=404)
    

#Obtener todas las mesas
def get_tables(request):
    profiles = Table.objects.all()

    profile_data = [{
                'id': profile.id,
                'outdoor': profile.outdoor,
                'status': profile.status,
                'number': profile.number,
                'bar': profile.bar,
                } for profile in profiles]

    return JsonResponse({'tables': profile_data}, safe=False)

#Obtener mesa por id
def get_table_by_id(request, table_id):
    try:
        profile = Advertisement.objects.get(id=table_id)
        profile_data = {
            'id': profile.id,
            'outdoor': profile.outdoor,
            'status': profile.status,
            'number': profile.number,
            'bar': profile.bar,
        }
        return JsonResponse({'table': profile_data})
    except Table.DoesNotExist:
        return JsonResponse({'error': 'Mesa no encontrada'}, status=404)


#Obtener todas las reservas
def get_bookings(request):
    profiles = Booking.objects.all()

    profile_data = [{
                'id': profile.id,
                'user': profile.user,
                'table': profile.table,
                'initial_datetime': profile.initial_datetime,
                'end_datetime': profile.end_datetime,
                'completed': profile.completed,
                } for profile in profiles]

    return JsonResponse({'bookings': profile_data}, safe=False)

#Obtener reserva por id
def get_booking_by_id(request, booking_id):
    try:
        profile = Booking.objects.get(id=booking_id)
        profile_data = {
            'id': profile.id,
            'user': profile.user,
            'table': profile.table,
            'initial_datetime': profile.initial_datetime,
            'end_datetime': profile.end_datetime,
            'completed': profile.completed,
        }
        return JsonResponse({'Booking': profile_data})
    except Booking.DoesNotExist:
        return JsonResponse({'error': 'Reserva no encontrada'}, status=404)