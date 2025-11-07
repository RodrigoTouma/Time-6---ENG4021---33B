from django.db import models

class MTCars(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(db_column='NAME')  # Nome do carro
    mpg = models.FloatField(db_column='MPG')   # Milhas por galão
    cyl = models.IntegerField(db_column='CYL') # Cilindros
    disp = models.FloatField(db_column='DISP') # Deslocamento
    hp = models.IntegerField(db_column='HP')   # Potência (horsepower)
    drat = models.FloatField(db_column='DRAT') # Relação diferencial
    wt = models.FloatField(db_column='WT')     # Peso
    qsec = models.FloatField(db_column='QSEC') # Tempo de 1/4 de milha
    vs = models.IntegerField(db_column='VS')   # Tipo de motor
    am = models.IntegerField(db_column='AM')   # Tipo de transmissão
    gear = models.IntegerField(db_column='GEAR') # Número de marchas

    class Meta:
        managed = True
        db_table = 'MTCars'
        ordering = ['id']

    def __str__(self):
        return f"Modelo: {self.name}"
