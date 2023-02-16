from django.db import models

# Create your models here.
class Test(models.Model):
    isPublic = models.BooleanField(default=True)
    tytul = models.CharField(max_length=100, blank=True, null=True)
    opis = models.CharField(max_length=500)
    hasloDostepu = models.CharField(max_length=30, blank=True, null=True)
    czyAktywny = models.BooleanField(default=True)
    owner = models.CharField(max_length=254)
    pokazWynik = models.BooleanField(default=True)
    pokazPoprawne = models.BooleanField(default=True)
    czasTrwania = models.IntegerField()
    terminOtwarcia = models.DateTimeField()
    terminZamkniecia = models.DateTimeField()

    def __str__(self):
        return f"Test id={self.id}"

class Pytanie(models.Model):
    numer = models.IntegerField()
    tresc = models.CharField(max_length=300)
    zamkniete = models.BooleanField(default=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)



class Odpowiedz(models.Model):
    tresc = models.CharField(max_length=300)
    czyPoprawna = models.BooleanField()
    pytanie = models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)


class Rozwiazanie(models.Model):
    ktoRozwiazal = models.CharField(max_length=254, blank=True, null=True)
    odpowiedz = models.CharField(max_length=1000)
    pytanie = models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)