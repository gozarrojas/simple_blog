from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'image_header')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'modified')

    # editamos el formulario, para que el usuario y el profile esten llenos
    def get_form(self, request, obj=None, change=False, **kwargs):
        # self.exclude = ('url',)
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        form.base_fields['profile'].initial = request.user.profile
        return form
