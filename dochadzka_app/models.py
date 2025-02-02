from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Neznáma kategória")  # Pridanie default hodnoty

    def __str__(self):
        return self.name


class Player(models.Model):
    jersey_number = models.IntegerField(unique=True)  # Unikátne číslo dresu
    first_name = models.CharField(max_length=50)  # Krstné meno hráča
    last_name = models.CharField(max_length=50)  # Priezvisko hráča
    birth_date = models.DateField()  # Dátum narodenia hráča
    email_1 = models.EmailField(unique=True)  # Primárny email
    email_2 = models.EmailField(blank=True, null=True)  # Sekundárny email (nepovinné)
    attendance_count = models.IntegerField(default=0)  # Počet absolvovaných tréningov
    all_training_count = models.IntegerField(default=0) # Počet možných absolvovaných tréningov
    categories = models.ManyToManyField(Category, related_name="players")  # Hráč môže byť vo viacerých kategóriách

    def __str__(self):
        return f"{self.jersey_number} - {self.first_name} {self.last_name} - {self.attendance_count}"
# Create your models here.
class Training(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="trainings")
    day=models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    players = models.ManyToManyField(Player, related_name="trainings")  # Výber hráčov na tréning

    def __str__(self):
        return f"{self.day} - {self.date} - {self.time}"

