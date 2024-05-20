from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import math
from .serializers import TableSerializer, UserProfileSerializer, BarSerializer, AdvertisementSerializer, BookingSerializer
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

#ZONA MESAS
@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated]) # TODO: Ver como hacer una validacion para que sea el bar sea el mismo que me esta pidiendo los datos
def process_tables_of_bar(request, id):
    if request.method == "GET":
        numero_personas = request.GET.get('numeroPersonas', None)
        exterior = request.GET.get('exterior')
        tables = Bar.objects.get(pk=id).table_set.all()
        if numero_personas and exterior is not None:
            numero_personas = int(numero_personas)
            tables = tables.filter(seats__gte=numero_personas, outdoor=(exterior.lower() == 'true'), status='FREE')
            tables = tables.order_by('seats')
            serializer = TableSerializer(data=tables, many=True)
            serializer.is_valid()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = TableSerializer(data=tables, many=True)
            serializer.is_valid()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        bar = Bar.objects.get(pk=id)
        serializer = TableSerializer(data={'bar': bar.id, 'number': request.data["number"], 'status': 'FREE', 'seats': request.data['seats'], 'outdoor': request.data['outdoor']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(None, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE','PATCH'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated]) # TODO: Ver como hacer una validacion para que sea el bar sea el mismo dueño que quiere borrar el anuncio
def delete_or_changue_table_of_bar(request, bar_id,table_id):
    if request.method == "DELETE":
        table = Table.objects.get(pk=table_id)
        table.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PATCH":
        table = Table.objects.get(pk=table_id)
        new_status = request.data.get('newStatus') 
        if new_status is None:
            table.status = 'PENDING_OF_CONFIRMATION'
            table.save()
            return Response({"message": "La mesa ha quedado reservada"}, status=status.HTTP_200_OK)
        else:
            if table.status == 'PENDING_OF_CONFIRMATION' and new_status == 'FREE':
                booking_sin_completar = [ x for x in table.booking_set.all() if x.completed is None or not x.completed ]
                if len(booking_sin_completar) > 0: # en realidad solo puede haber un booking activo
                    diff = timezone.now() - booking_sin_completar[0].initial_datetime
                    minutes_diff = diff.total_seconds() / 60
                    if minutes_diff > 20:
                        booking_sin_completar[0].delete()
                        table.status = new_status
                        table.save()
                        return Response({"message": "Estado de la mesa actualizado correctamente de PENDING_OF_CONFIRMATION a FREE"}, status=status.HTTP_200_OK)
                    else:
                        return Response({"message": "Debes dar de cortesia 20 minutos antes de cancelar la reserva..."}, status=status.HTTP_409_CONFLICT)
            elif table.status == 'BUSY' and new_status == 'FREE':
                booking_sin_completar = [ x for x in table.booking_set.all() if x.completed is None or not x.completed ]
                if len(booking_sin_completar) > 0: # en realidad solo puede haber un booking activo
                    booking_sin_completar[0].end_datetime = timezone.now()
                    booking_sin_completar[0].save()
                table.status = new_status
                table.save()
                return Response({"message": "Estado de la mesa actualizado correctamente de BUSY a FREE"}, status=status.HTTP_200_OK)
            elif table.status == 'PENDING_OF_CONFIRMATION' and new_status == 'BUSY':
                booking_sin_completar = [ x for x in table.booking_set.all() if x.completed is None or not x.completed ]
                if len(booking_sin_completar) > 0: 
                    booking_sin_completar[0].completed = True
                    booking_sin_completar[0].save()
                table.status = new_status
                table.save()
                return Response({"message": "Estado de la mesa actualizado correctamente de PENDING_OF_CONFIRMATION a BUSY"}, status=status.HTTP_200_OK)
            elif table.status == 'FREE' and new_status == 'BUSY':
                table.status = new_status
                table.save()
                return Response({"message": "Estado de la mesa actualizado correctamente de FREE a BUSY"}, status=status.HTTP_200_OK)
            

#ZONA ANUNCIOS
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
        serializer = BarSerializer(bar_info, data={
            'id': bar_info.id,
            'name': request.data['recordData']['name'], 
            'description': request.data['recordData']["description"],
            'phone': request.data['recordData']['phone'], 
            'address': request.data['recordData']['address'], 
            'latitude': request.data['recordData']['latitude'], 
            'longitude': request.data['recordData']['longitude']
        }, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(None, status=status.HTTP_405_METHOD_NOT_ALLOWED)


#ZONA INFO CUENTA USUARIO PLANO
@api_view(['GET','PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated]) # TODO: Ver como hacer una validacion url
def process_data_of_user(request, id):
    if request.method == "GET":
        user_info = UserProfile.objects.get(pk=id)
        serializer = UserProfileSerializer(user_info)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        user_info = UserProfile.objects.get(pk=id)
        serializer = UserProfileSerializer(user_info, data={
            'id': user_info.id,
            'fullname': request.data['recordData']['fullname'], 
            'phone': request.data['recordData']['phone'], 
            'birthdate': request.data['recordData']['birthdate']
        }, partial=True)
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
    

#ZONA RESERVA ACCION/REACCION

#funcion calcular area donde se encuentran bares disponibles
def calcular_area(latitud_usuario, longitud_usuario, distancia_km):
    # Calcula las variaciones en latitud y longitud
    latitud_variation = distancia_km / 111  # 1 grado de latitud es aproximadamente 111 km
    longitud_variation = distancia_km / (111 * math.cos(math.radians(latitud_usuario)))

    # Calcula las coordenadas del área de búsqueda
    latitud_superior = latitud_usuario + latitud_variation
    latitud_inferior = latitud_usuario - latitud_variation
    longitud_derecha = longitud_usuario + longitud_variation
    longitud_izquierda = longitud_usuario - longitud_variation

    return latitud_superior, latitud_inferior, longitud_derecha, longitud_izquierda


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_bars(request):
    if request.method == "GET":
        if request.GET:
            map_center = request.GET.get('mapCenter', '').split(',')
            distancia = float(request.GET.get('distancia', 0))
            exterior = request.GET.get('exterior', '').lower() == 'true'
            numero_personas = int(request.GET.get('numeroPersonas', 0))
            # Verifica que los parámetros necesarios estén presentes
            if not map_center or not distancia:
                return JsonResponse({'error': 'Parámetros faltantes'}, status=400)
            try:
                # Convierte los elementos de map_center a valores de latitud y longitud
                latitud_str, longitud_str= map_center
                latitud = float(latitud_str)
                longitud = float(longitud_str)
                # Calcula el área de búsqueda
                latitud_superior, latitud_inferior, longitud_derecha, longitud_izquierda = \
                calcular_area(latitud, longitud, distancia)
                bares_en_area = Bar.objects.filter(
                    latitude__range=(latitud_inferior, latitud_superior),
                    longitude__range=(longitud_izquierda, longitud_derecha),
                    table__seats__gte=numero_personas,
                    table__outdoor=exterior,
                    table__status='FREE'
                ).distinct()
                # Crea una lista de diccionarios para los resultados
                results = [{'id': bar.id,'name': bar.name,'description': bar.description,'phone': bar.phone, 'address': bar.address, 'latitude': bar.latitude, 'longitude': bar.longitude}
                    for bar in bares_en_area]
                print(results)
                return Response(results, status=status.HTTP_200_OK)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error al traer bares'}, status=400)



#ZONA RESERVAS
#Crear reserva por ususario
#ZONA ANUNCIOS
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated]) # TODO: Ver como hacer una validacion para que sea el bar sea el mismo que me esta pidiendo los datos
def create_booking_by_user(request, user_id, table_id):
    if request.method == "POST":
        booking_data = {
            "user": user_id,
            "table": table_id,
            "initial_datetime": timezone.now(),
            "end_datetime": None
        }
        serializer = BookingSerializer(data=booking_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(None, status=status.HTTP_405_METHOD_NOT_ALLOWED)


#COMPROBAR RESERVAS DEL USUARIO
@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_booking_by_user(request,id):
    user_profile = get_object_or_404(UserProfile, pk=id)
    user_bookings = user_profile.booking_set.filter(completed__isnull=True)
    serializer = BookingSerializer(user_bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    

##ZONA USUARIO ADMINISTRADOR
#Obtener todos los bares
@api_view(['GET'])
def get_all_bars(request):
    if request.method == 'GET':
        try:
            # Obtenemos todos los objetos Bar de la base de datos
            bars = Bar.objects.all()
            # Serializamos los objetos Bar para enviarlos como respuesta
            serializer = BarSerializer(bars, many=True)
            print(serializer.data)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

#Obtener los bares por id del bar
@api_view(['GET'])
def get_bookings_by_bar(request, bar_id):
    try:
        bookings = Booking.objects.filter(table__bar_id=bar_id)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Booking.DoesNotExist:
        return Response({"error": "No bookings found for this bar"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





















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