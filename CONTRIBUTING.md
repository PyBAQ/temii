# ¿Cómo Contribuir?

Existen muchas formas en las que puedes contribuir a *Temii*.

Contribuyendo con código, escribiendo documentación, reportando errores, así
como leyendo y proporcionando tus comentarios a issues y pull-requests (PR),
todas son maneras necesarias y validas de ayudar.

Si deseas colaborar con código fuente, es importante tener en cuenta las
siguientes recomendaciones, que permitirán tener un control de los cambios que
se implementen y nos permita trabajar bajo los mismos lineamientos.

## Haciendo cambios en el código

Al ser *Temii* un proyecto abierto, todos pueden contribuir con sus cambios e
integrarlos al repositorio principal de una forma fácil.

Para esto recomendamos que todo el trabajo que hagas, lo realices en una rama
(branch) aparte. Cuando estés listo para trabajar en un error o en una nueva
característica, crea una rama (branch). La razón por la que esto es importante es
que puedes hacer tantos commits como consideres necesario. Cuando estés listo
puedes mezclarlos. Miremos como es el flujo básico:

    git checkout –b task-556
    … fix and git commit often …
    git push origin task-556

La razón por la que hemos creado dos ramas, es con el fin de mantenernos
alejados de la principal (master). Mantener la rama master limpia para los cambios
provenientes del repositorio principal (upstream) hace tu vida y la nuestra más
sencilla. Puedes enviarnos un pull request de tus cambios. Nosotros lo
revisaremos e integraremos al repositorio base.

Ten muy en cuenta los [Estilos de codificación](#Estilo-de-codificación), debido
a que pueden ser la causa de un rechazo a un pull-requests.

## Estilo de codificación

Cuando vayas a escribir código que quieras que sea incluido en *Temii*, ten
en cuenta el estilo de codificación que utilizas.

Estaremos validando que el código propuesto, cumpla con la mayoría de las reglas
definidas a continuación y en determinado momento, el no cumplir con estos
estilos puede generar un rechazo de tu PR.

> - Sigue los lineamientos del [PEP8][1]
> - Sigue las [guías de estilo de Django][2]

Este es un ejemplo de estas reglas aplicadas:

	# Primer grupo de imports "stdlib"
	# no-from imports van de primero y luegos los from en su propio grupo
	import csv

	# Segundo grupo de imports son los de Django con los contrib en su propio grupo.
	from django.core.urlresolvers import reverse
	from django.db import models
	from django.utils import timezone
	from django.utils.translation import ugettext_lazy as _

	from django.contrib.auth.models import User

	# Tercer grupo son los imports de aplicaciones de terceros (si aplica)
	from tagging.fields import TagField

	# Cuarto grupo son los imports de aplicaciones locales
	from .fields import MarkupField

	class Task(models.Model):
    """
    A model for storing a task.
    """

    creator = models.ForeignKey(User)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")

    def __unicode__(self):
        return self.summary

    def save(self, \**kwargs):
        self.modified = datetime.now()
        super(Task, self).save(\**kwargs)

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"task_id": self.pk})

    # metodos personalizados

## Pull Requests

Por favor mantén tus pull requests enfocados en un solo tema en específico.
Si tienes un número de solicitudes por enviar, entonces envía solicitudes
separadas. Es mucho más fácil recibir solicitudes pequeñas y bien definidas, que
tener que revisar y gestionar solicitudes grandes que apuntan a diferentes
temas.

Si terminas haciendo varios commits para un solo cambio (asociado a un tema
en particular), por favor, re-organízalo en un solo commit:

```sh
$ git rebase -i HEAD~10  # donde 10 es el número de commits que necesitas.
```

Esto abrirá un editor con tus  commits y algunas instrucciones que necesitas
seguir para poder escoger los commits que quieres integrar reemplazando ‘pick’
por ‘s’ para combinarlos con un commit previo.

Cuando guardes y salgas del editor donde estuviste combinando los commits, git
los combinará y te mostrará otro editor con los mensajes de commit. Escoge el
mensaje con el que quieres que quede el cambio (o escribe uno nuevo).
Guarda y sal para completar esta acción. Usa un push forzado a
tu repositorio (fork).

```sh
git push -f
```

[1]: https://www.python.org/dev/peps/pep-0008/
[2]: https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/
