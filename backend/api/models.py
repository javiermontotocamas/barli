from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator
from django.core.exceptions import ValidationError



class UserProfile(models.Model):
    def validate_phone(value):
        phone_regex = r'^\+?1?\d{9,15}$'
        validator = RegexValidator(regex=phone_regex, message="Formato de teléfono no válido,permite números de teléfono con un formato que empiece con un signo más opcional (+), seguido opcionalmente por el código de país 1, y luego de 9 a 15 dígitos adicionales.")
        validator(value)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=30,validators=[validate_phone])
    birthdate = models.DateField()

    def __str__(self) -> str:
        return f"{self.fullname}"


class Bar(models.Model):
    def validate_phone(value):
        phone_regex = r'^\+?1?\d{9,15}$'
        validator = RegexValidator(regex=phone_regex, message="Formato de teléfono no válido,permite números de teléfono con un formato que empiece con un signo más opcional (+), seguido opcionalmente por el código de país 1, y luego de 9 a 15 dígitos adicionales.")
        validator(value)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True,max_length=255)
    phone = models.CharField(max_length=30, validators=[validate_phone])
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

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

    def __str__(self) -> str:
        return f"Num: {self.number} - Bar: {self.bar.name} - Seats: {self.seats}"



class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    initial_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    completed = models.BooleanField()

    class Meta:
        unique_together = ('table', 'initial_datetime',)
        constraints = [
            models.CheckConstraint(
                check=models.Q(end_datetime__gt=models.F('initial_datetime')),
                name="end_datetime_check"
            )
        ]




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