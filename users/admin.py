from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #Que debemos mostrar
    list_display = ('pk','user','photo')
    #En donde debemos haces click para editarlo
    list_display_links = ('user',)
    #Permite editar en la misma pagina
    list_editable = ('photo',)

    #habilita una barra de busqueda, e indica con que valor buscar
    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'data_modified',
    )

    fieldsets = (
        ('Información del Perfil',{
            'fields':('user','photo','website',)
        }),
    )

#Editar modelos en la misma página que un modelo principal.
#Definimos el modelo que queremos añadir al modelo padre
# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profiles'
#
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline,)
#     list_display = (
#         'username',
#         'email',
#         'first_name',
#         'last_name',
#         'is_active',
#         'is_staff'
#     )
#
# admin.site.unregister(User)
# admin.site.register(User,UserAdmin)