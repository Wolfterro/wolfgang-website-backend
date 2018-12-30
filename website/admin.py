from django.contrib import admin
from django.conf import settings

from website.models import Info, Block, SocialMedia, File, Button


# Register your models here.
# ==========================
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ("owner", "occupation", "additional_info", )

    def has_add_permission(self, request):
        return False if Info.objects.count() > 0 else super().has_add_permission(request)


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    def has_image(self, obj):
        return "Sim" if obj.image is not None else "Não"
    has_image.short_description = "Possui Imagem?"

    def has_button(self, obj):
        return "Sim" if obj.button is not None else "Não"
    has_button.short_description = "Possui botão?"

    list_display = ("title", "content", "order", "background_color", "has_image", "has_button", )
    ordering = ("order", )


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "linkedin", "github", "facebook", "instagram", "youtube", )

    def has_add_permission(self, request):
        return False if SocialMedia.objects.count() > 0 else super().has_add_permission(request)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    def url(self, obj):
        return "{0}{1}".format(settings.BACKEND_ADDRESS, obj.file.url)
    url.short_description = "URL"

    list_display = ("name", "url", )


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ("text", "type", "link", "size", )

    def get_model_perms(self, request):
        return {}
