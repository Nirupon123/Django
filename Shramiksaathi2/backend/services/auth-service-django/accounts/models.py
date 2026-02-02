from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.gis.db import models as geomodels
from django.db import models
from django.utils import timezone

class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    aadhar = models.CharField(max_length=20, blank=True, null=True)



    ROLE_CHOICES = [
        ("worker", "Worker"),
        ("employer", "Employer"),
        ("NGO", "NGO"),
    ]
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="worker"
    )

    location = geomodels.PointField(
        geography=True,
        blank=True,
        null=True
    )

    rating = models.FloatField(default=1.0)
    address = models.TextField(blank=True, null=True)

    community = models.ForeignKey(
        "Community",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="users"
    )

    points = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    #auth config
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone"]

    def __str__(self):
        return self.email
