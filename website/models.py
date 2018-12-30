from django.db import models
from django.conf import settings

from ckeditor.fields import RichTextField


# Create your models here.
# ========================
class Info(models.Model):
    owner = models.CharField(max_length=150, default="", verbose_name="Dono do Website")
    occupation = models.CharField(max_length=150, default="", verbose_name="Ocupação")
    additional_info = models.CharField(max_length=255, default="", verbose_name="Informações Adicionais",
                                       blank=True, null=True)
    jumbotron_image = models.ImageField(default=None, verbose_name="Jumbotron", upload_to="img")

    def __str__(self):
        return self.owner

    def get_json(self):
        return {
            "id": self.id,
            "owner": self.owner,
            "occupation": self.occupation,
            "additional_info": self.additional_info,
            "jumbotron_image": "{0}{1}".format(settings.BACKEND_ADDRESS, self.jumbotron_image.url) if self.jumbotron_image else None
        }

    class Meta:
        verbose_name = "Informação Principal"
        verbose_name_plural = "Informações Principais"



class Block(models.Model):
    BACKGROUND_COLOR_CHOICES = (
        ("0097dc", "Light Blue"),
        ("0186c4", "Dark Blue")
    )

    title = models.CharField(max_length=150, default="", verbose_name="Título")
    content = RichTextField(default="", verbose_name="Conteúdo")
    image = models.ImageField(default=None, blank=True, null=True, verbose_name="Imagem", upload_to="img")

    background_color = models.CharField(max_length=6, default="", choices=BACKGROUND_COLOR_CHOICES,
                                        verbose_name="Cor de Fundo")
    order = models.IntegerField(default=0, verbose_name="Ordem")
    button = models.ForeignKey("Button", on_delete=models.CASCADE, verbose_name="Botão", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "image": "{0}{1}".format(settings.BACKEND_ADDRESS, self.image.url) if self.image else None,
            "background_color":  self.background_color,
            "order": self.order,
            "button": self.button.get_json() if self.button else None
        }

    class Meta:
        verbose_name = "Bloco de Conteúdo"
        verbose_name_plural = "Blocos de Conteúdos"


class SocialMedia(models.Model):
    email = models.EmailField(default="", verbose_name="E-Mail")
    linkedin = models.URLField(default="", verbose_name="LinkedIn")
    github = models.URLField(default="", verbose_name="GitHub")

    facebook = models.URLField(default="", verbose_name="Facebook", blank=True, null=True)
    instagram = models.URLField(default="", verbose_name="Instagram", blank=True, null=True)
    youtube = models.URLField(default="", verbose_name="Youtube", blank=True, null=True)

    def __str__(self):
        return "Redes Sociais"

    def get_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "linkedin": self.linkedin,
            "github": self.github,
            "facebook": self.facebook,
            "instagram": self.instagram,
            "youtube": self.youtube
        }

    class Meta:
        verbose_name = "Rede Social"
        verbose_name_plural = "Redes Sociais"


class File(models.Model):
    name = models.CharField(max_length=150, default="", verbose_name="Nome")
    file = models.FileField(upload_to="files", verbose_name="Arquivo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Arquivo"
        verbose_name_plural = "Arquivos"


class Button(models.Model):
    BUTTON_TYPES_CHOICES = (
        ("btn", "Basic"),
        ("btn btn-primary", "Primary"),
        ("btn btn-secondary", "Secondary"),
        ("btn btn-success", "Success"),
        ("btn btn-info", "Info"),
        ("btn btn-warning", "Warning"),
        ("btn btn-danger", "Danger"),
        ("btn btn-dark", "Dark"),
        ("btn btn-light", "Light"),
        ("btn btn-link", "Link"),
    )

    BUTTON_SIZE_CHOICES = (
        ("btn-lg", "Grande"),
        ("", "Normal"),
        ("btn-sm", "Pequeno")
    )

    BUTTON_ICONS_CHOICES = (
        ("fas fa-download", "Download"),
        ("fas fa-file-pdf", "Arquivo PDF"),
        ("far fa-file", "Arquivo Comum")
    )

    text = models.CharField(max_length=150, default="", verbose_name="Texto")
    type = models.CharField(max_length=32, default="", choices=BUTTON_TYPES_CHOICES, verbose_name="Tipo")
    link = models.URLField(default="", verbose_name="Link")
    size = models.CharField(max_length=8, default="", choices=BUTTON_SIZE_CHOICES, verbose_name="Tamanho")

    left_icon = models.CharField(max_length=32, default="", choices=BUTTON_ICONS_CHOICES,
                                 verbose_name="Ícone Esquerdo")
    right_icon = models.CharField(max_length=32, default="", choices=BUTTON_ICONS_CHOICES,
                                  verbose_name="Ícone Direito")

    def __str__(self):
        return self.text

    def get_json(self):
        return {
            "text": self.text,
            "type": self.type,
            "link": self.link,
            "size": self.size,
            "left_icon": self.left_icon,
            "right_icon": self.right_icon
        }

    class Meta:
        verbose_name = "Botão"
        verbose_name_plural = "Botões"
