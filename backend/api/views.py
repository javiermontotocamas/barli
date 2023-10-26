from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import *


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