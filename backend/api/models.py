from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator,MaxLengthValidator
from django.core.exceptions import ValidationError
from datetime import date



class UserProfile(models.Model):
    def validate_name(value):
        max_length_validator = MaxLengthValidator(limit_value=20)
        max_length_validator(value)
    def validate_phone(value):
        phone_regex = r'^\+?1?\d{9,15}$'
        validator = RegexValidator(regex=phone_regex, message="Formato de teléfono no válido,permite números de teléfono con un formato que empiece con un signo más opcional (+), seguido opcionalmente por el código de país 1, y luego de 9 a 15 dígitos adicionales.")
        validator(value)
    def validate_age(value):
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 14:
            raise ValidationError("Debes tener al menos 14 años para registrarte.")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255,validators=[validate_name])
    phone = models.CharField(max_length=30,validators=[validate_phone])
    birthdate = models.DateField(validators=[validate_age])

    def __str__(self) -> str:
        return f"{self.fullname}"


class Bar(models.Model):
    def validate_name(value):
        max_length_validator = MaxLengthValidator(limit_value=20)
        max_length_validator(value)
    def validate_description(value):
        max_length_validator = MaxLengthValidator(limit_value=255)
        max_length_validator(value)
    def validate_phone(value):
        phone_regex = r'^\+?1?\d{9,15}$'
        validator = RegexValidator(regex=phone_regex, message="Formato de teléfono no válido,permite números de teléfono con un formato que empiece con un signo más opcional (+), seguido opcionalmente por el código de país 1, y luego de 9 a 15 dígitos adicionales.")
        validator(value)
    def validate_address(value):
        max_length_validator = MaxLengthValidator(limit_value=100)
        max_length_validator(value)
    def validate_latitude(value):
        regex = r'^[+-]?(?:3[6-9]|4[0-3])\.\d{1,6}$'
        validator = RegexValidator(regex=regex, message="Formato de latitud no válido, esta aplicación está pensada para bares en territorio español, cuyas latitudes peninsulares comprenden de la 36 al 43.")
        validator(value)
    def validate_longitude(value):
        regex = r'^[+-]?(?:-[0-9]|0|1|2|3|4)\.\d{1,6}$'
        validator = RegexValidator(regex=regex, message="Formato de longitud no válido, esta aplicación está pensada para bares en territorio español, cuyas longitudes peninsulares comprenden de la -9 al 4.")
        validator(value)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20,validators=[validate_name])
    description = models.TextField(null=True, blank=True,max_length=255,validators=[validate_description])
    phone = models.CharField(max_length=30, validators=[validate_phone])
    address = models.CharField(max_length=100, validators=[validate_address])
    latitude = models.DecimalField(max_digits=9, decimal_places=6, validators=[validate_latitude])
    longitude = models.DecimalField(max_digits=9, decimal_places=6, validators=[validate_longitude])

    def __str__(self) -> str:
        return f"{self.name}"


class Advertisement(models.Model):
    class Meta:
        unique_together = ('bar', 'product_name',)

    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    reduction = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(5), MaxValueValidator(95)])

    def __str__(self) -> str:
        return f"{self.bar} - {self.product_name}"


class Table(models.Model):
    class Meta:
        unique_together = ('number', 'bar',)

    class TableStatus(models.TextChoices):
        FREE = ("FREE", "Free")
        PENDING_OF_CONFIRMATION = ("PENDING_OF_CONFIRMATION", "Pending of confirmation")
        BUSY = ("BUSY", "Busy")

    seats = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    outdoor = models.BooleanField()
    status = models.CharField(max_length=255, choices=TableStatus.choices, default=TableStatus.FREE)
    number = models.SmallIntegerField()
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)

    def active_bookings(self):
        return Booking.objects.filter(table=self, completed__isnull=True)

    def __str__(self) -> str:
        return f"Num: {self.number} - Bar: {self.bar.name} - Seats: {self.seats}"



class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    initial_datetime = models.DateTimeField()
    end_datetime = models.DateField(null=True, blank=True)
    completed = models.BooleanField(null=True)

    class Meta:
        unique_together = ('table', 'initial_datetime',)
        constraints = [
            models.CheckConstraint(
                check=models.Q(end_datetime__gt=models.F('initial_datetime')),
                name="end_datetime_check"
            )
        ]

    def __str__(self) -> str:
        return f"User: {self.user.fullname} - Bar: {self.table.bar.name} - Table: {self.table.number} - Completed: {self.completed} - Date: {self.initial_datetime}"


def find_userprofile_by_django_user_id(user_id):
    try:
        profile = UserProfile.objects.get(user__id=user_id)
    except UserProfile.DoesNotExist:
        profile = None

    return profile


def find_bar_by_django_user_id(user_id):
    try:
        bar = Bar.objects.get(user__id=user_id)
    except Bar.DoesNotExist:
        bar = None

    return bar


def find_user_or_bar_and_role_by_django_user_id(user_id):
    result = find_userprofile_by_django_user_id(user_id)
    if result:
        return (result, "user")
    
    result = find_bar_by_django_user_id(user_id)
    if result:
        return (result, "bar")
    
    return None