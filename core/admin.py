from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django import forms
from .models import Receitas, Despesas

Usuario = get_user_model()


class UsuarioCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmação de Senha", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ("email",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UsuarioChangeForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ("email", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")


@admin.register(Usuario)
class UsuarioAdmin(DjangoUserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario

    list_display = ("email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "is_superuser", "groups")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {"fields": ("email", "password1", "password2", "is_staff", "is_active")}),
    )

    filter_horizontal = ("groups", "user_permissions")

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('IdCondominio', 'NomeCondominio', 'Unidade', 'Valor', )
    search_fields = ('NomeCondominio', 'Unidade')

admin.site.register(Receitas, ReceitaAdmin)

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('Condominio', 'Fornecedor', 'Valor', )
    search_fields = ('Condominio', 'Fornecedor')

admin.site.register(Despesas, DespesaAdmin)

