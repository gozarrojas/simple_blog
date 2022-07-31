from django.contrib import admin
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Que debemos mostrar
    list_display = ('pk', 'user', 'photo')
    # En donde debemos haces click para editarlo
    list_display_links = ('user',)
    # Permite editar en la misma pagina
    list_editable = ('photo',)

    # habilita una barra de busqueda, e indica con que valor buscar
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
