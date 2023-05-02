from django.core.validators import FileExtensionValidator
from django.db import models


class Services(models.Model):
    title = models.CharField(verbose_name="Nome do Serviço", max_length=64)
    smalldesc = models.TextField(
        verbose_name="Descrição curta",
    )
    largedesc = models.TextField(
        verbose_name="Descrição longa",
    )
    icon = models.FileField(
        verbose_name="Ícone do Serviço",
        upload_to="services/",
        validators=[FileExtensionValidator(["svg"])],
        help_text="O arquivo necessita ser do tipo SVG.",
        blank=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        app_label = "api"
