from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo "email" é obrigatório.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    TIPO_USUARIO = [
        ('gestao', 'Gestão Condominial'),
        ('contabilidade', 'Contabilidade'),
    ]

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    precisa_redefinir_senha = models.BooleanField(default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"
    
class Receitas(models.Model):
    IdCondominio = models.IntegerField()
    NomeCondominio = models.CharField(max_length=255)
    Unidade = models.CharField(max_length=50)
    Contato = models.CharField(max_length=255)
    Cobranca = models.IntegerField()
    DescricaoTaxa = models.CharField(max_length=255)
    Complemento = models.CharField(max_length=255, blank=True, null=True)
    Geracao = models.DateField()
    Vencimento = models.DateField()
    Liquidacao = models.DateField(blank=True, null=True)
    Credito = models.DateField(blank=True, null=True)
    FormaPagamento = models.CharField(max_length=100, blank=True, null=True)
    Valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.NomeCondominio} - {self.Unidade} - {self.Valor}"


class Despesas( models.Model):
    Condominio = models.CharField(max_length=255)
    Vencimento = models.DateField()
    Liquidacao = models.DateField(blank=True, null=True)
    Fornecedor = models.CharField(max_length=255)
    Categoria = models.CharField(max_length=255)
    Complemento = models.CharField(max_length=255, blank=True, null=True)
    Documento = models.CharField(max_length=100)
    Competencia = models.DateField()
    FormaPagamento = models.CharField(max_length=100, blank=True, null=True)
    Valor = models.DecimalField(max_digits=10, decimal_places=2)
