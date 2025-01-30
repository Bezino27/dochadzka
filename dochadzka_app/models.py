from django.db import models

class Player(models.Model):
    jersey_number = models.IntegerField(unique=True)  # Unikátne číslo dresu
    first_name = models.CharField(max_length=50)  # Krstné meno hráča
    last_name = models.CharField(max_length=50)  # Priezvisko hráča
    birth_date = models.DateField()  # Dátum narodenia hráča
    email_1 = models.EmailField(unique=True)  # Primárny email
    email_2 = models.EmailField(blank=True, null=True)  # Sekundárny email (nepovinné)
    attendance_count = models.IntegerField(default=0)  # Počet absolvovaných tréningov

    def __str__(self):
        return f"{self.jersey_number} - {self.first_name} {self.last_name} - {self.attendance_count}"
# Create your models here.
