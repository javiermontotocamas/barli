from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    birthdate = models.DateField()

    def __str__(self) -> str:
        return f"{self.fullname}"


class Bar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class Advertisement(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    reduction = models.DecimalField(max_digits=5, decimal_places=2)


class Table(models.Model):
    class TableStatus(models.TextChoices):
        FREE = ("FREE", "Free")
        PENDING_OF_CONFIRMATION = ("PENDING_OF_CONFIRMATION", "Pending of confirmation")
        BUSY = ("BUSY", "Busy")

    seats = models.SmallIntegerField()
    outdoor = models.BooleanField()
    status = models.CharField(max_length=255, choices=TableStatus.choices, default=TableStatus.FREE)
    number = models.SmallIntegerField()
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('number', 'bar',)


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


def find_role_by_django_user_id(user_id):
    if find_userprofile_by_django_user_id(user_id):
        return "user"
    
    if find_bar_by_django_user_id(user_id):
        return "bar"
    
    return None