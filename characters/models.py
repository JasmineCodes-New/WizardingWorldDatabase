from django.db import models  # For storing lists in PostgreSQL


#class AlternateName(models.Model):
   # character = models.ForeignKey('Character', on_delete=models.CASCADE)
    #name = models.CharField(max_length=100)


class Character(models.Model):
    character_id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
 #   alternate_names = models.CharField(max_length=255, null=True, blank=True)
    species = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    house = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.CharField(max_length=20, null=True, blank=True)
    year_of_birth = models.IntegerField(null=True, blank=True)
    wizard = models.BooleanField(null=True)
    ancestry = models.CharField(max_length=50, null=True, blank=True)
    eye_color = models.CharField(max_length=20, null=True, blank=True)
    hair_color = models.CharField(max_length=20, null=True, blank=True)
    patronus = models.CharField(max_length=100, null=True, blank=True)
    hogwarts_student = models.BooleanField(null=True)
    hogwarts_staff = models.BooleanField(null=True)
    actor = models.CharField(max_length=100, null=True, blank=True)
    alive = models.BooleanField(null=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Wand(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    wood = models.CharField(max_length=50)
    core = models.CharField(max_length=50)
    length = models.IntegerField()

    def __str__(self):
        return f"{self.wood} wood, {self.core} core, {self.length}\""
