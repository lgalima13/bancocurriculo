from django.db import models
from django.conf import settings

class Profile(models.Model):
    CARTEIRACATEGORIA_CHOICES = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('e', 'E'),
        ('ab', 'AB'),
        ('ac', 'AC'),
        ('ad', 'AD'),
        ('ae', 'AE'),
    )
    ESTADOCIVIL_CHOICES = (
        ('so', 'SOLTEIRO(A)'),
        ('ca', 'CASADO(A)'),
        ('se', 'SEPARADO(A)'),
        ('di', 'DIVORCIADO(A)'),
        ('vi', 'VIÚVO(A)'),
    )
    AREAINTERESSE_CHOICES = (
        ('ad', 'ADMINISTRATIVA'),
        ('te', 'TÉCNICA'),
        ('cm', 'COMERCIAL'),
        ('tr', 'TRANSPORTES'),
        ('op', 'OPERACIONAL'),
        ('sg', 'SERVIÇOS GERAIS'),
        ('rh', 'RECURSOS HUMANOS'),
        ('pg', 'PROGRAMAÇÃO'),
        ('jn', 'JORNALÍSTICA'),
    )
    ESCOLARIDADE_CHOICES = (
        ('fundai', 'Fundamental Incompleto'),
        ('fundac', 'Fundamental Completo'),
        ('medioi', 'Ensino Médio Completo'),
        ('medioc', 'Ensino Médio Incompleto'),
        ('superi', 'Superior Incompleto'),
        ('superc', 'Superior Completo'),
        ('posgra', 'Pós-Graduação'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    datanascimento = models.DateField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    estadocivil = models.CharField(verbose_name='Estado Civil',
                                   max_length=2,
                                   choices=ESTADOCIVIL_CHOICES,
                                   blank=True,
                                   null=True)
    necessidade = models.BooleanField(default=False)
    necessidadecategoria = models.CharField(max_length=255, blank=True, null=True)
    carteira = models.BooleanField(default=False)
    carteiracategoria = models.CharField(verbose_name='Se sim, Qual a categoria?',
                                         max_length=2,
                                         choices=CARTEIRACATEGORIA_CHOICES,
                                         blank=True,
                                         null=True)
    areainteresse = models.CharField(verbose_name='Qual a área do seu interesse?',
                                     max_length=2,
                                     choices=AREAINTERESSE_CHOICES,
                                     blank=True,
                                     null=True)
    escolaridade = models.CharField(verbose_name='Grau de escolaridade',
                                    max_length=6,
                                    choices=ESCOLARIDADE_CHOICES,
                                    blank=True,
                                    null=True)
    instituicao = models.TextField(blank=True, null=True)
    empresa1 = models.CharField(max_length=150, blank=True, null=True)
    empresa2 = models.CharField(max_length=150, blank=True, null=True)
    empresa3 = models.CharField(max_length=150, blank=True, null=True)
    cargo1 = models.CharField(max_length=150, blank=True, null=True)
    cargo2 = models.CharField(max_length=150, blank=True, null=True)
    cargo3 = models.CharField(max_length=150, blank=True, null=True)
    atividades1 = models.TextField(blank=True, null=True)
    atividades2 = models.TextField(blank=True, null=True)
    atividades3 = models.TextField(blank=True, null=True)
    datainicio1 = models.DateField(blank=True, null=True)
    datainicio2 = models.DateField(blank=True, null=True)
    datainicio3 = models.DateField(blank=True, null=True)
    datasaida1 = models.DateField(blank=True, null=True)
    datasaida2 = models.DateField(blank=True, null=True)
    datasaida3 = models.DateField(blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    aceitetermos = models.BooleanField(default=False)

    def __str__(self):
        return f'Profile for user {self.user.username}'
