# temii

Aplicación web para elegir las futuras charlas del meetup de Python Barranquilla

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: Apache Software License 2.0

## Variables de entorno

Este proyecto, creado con cokkiecutter permite cambiar un monton de ajustes usando variables de entorno
[para ver estos ajustes abre este enlace](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Comandos básicos

### Ejecutar docker-compose localmente

Para ejecutar docker compose localmente toca especificarle que use el archivo local.yml

    docker compose -f local.yml up

### Crear usuarios

- Para crear un **usuario normal**, ve a Sign Up y llena los campos del formulario, luego veras la página para confirmar el email, ve a la consola para ver un mensaje de correo simulado, copia el link en tu navegador web. Ahora el correo del usuario estará verificado y listo para usar.

- Para crear una **cuenta de superadministrador**, usa el comando:

```bash
docker compose -f local.yml run --rm django python manage.py shell_plus

python manage.py createsuperuser
```

Por conveniencia, puedes abrir el usuario normal en un navegador, y el super-administrador en otro y ver los comportamientos para cada tipo de usuario.

### Type checks

Puedes correr los checks de tipos de datos con el comando

    mypy temii

### Debugging con ipdb

Levanta los contenedores de forma _detached_, detén el de django y luego habilita el puerto donde corre. De la siguiente manera:

```bash
docker compose -f local.yml up -d
docker compose -f local.yml down django
docker compose -f local.yml run --rm --service-ports django
```

De esta forma podrás usar `import ipdb; ipdb.set_trace()` en tu código de Python sin problemas.

### Cobertura de pruebas

Para ejecutar los tests, verificar el coverage y generar un reporte de coverage en HTML:

    docker compose -f local.yml run --rm django coverage run -m pytest
    docker compose -f local.yml run --rm django coverage html
    open htmlcov/index.html

#### Ejecutar los test usando pytest

    pytest

### Compilación de SASS y recarga en vivo (Live reloading)

Cookiecutter soporta la compilación de sass [Puedes ver como funciona en este enlace](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Sentry

Sentry es una herramienta para el manejo de logs, puedes crear una cuenta gratuita en el siguiente enlace <https://sentry.io/signup/?code=cookiecutter> o descargarlo y hospedarlo por ti mismo.
El sistema es configurado con algunas cosas por defecto, incluyendo, los logs de 404 e interacciónes con la aplicación WSGI.

Hay que configurar la url del DSN en producción.

## Despliegue

Estos son los detalles acerca de como desplegar esta aplicación.

### Docker

Vea [esta guia de configuración de cookiecutter-django con Docker](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### Contribuciones

Necesitamos de tu ayuda para terminar este proyecto! **¿Cómo puedes contribuir?** Mira las normas que hemos redactado en el archivo [CONTRIBUTING.md] para organizarnos mejor en el desarrollo. Esperamos tus Pull Requests e Issues. Gracias por tu apoyo.

[CONTRIBUTING.md]: https://github.com/DjangoQuilla/temii/blob/master/CONTRIBUTING.md

### Licencia

[Apache License 2.0](LICENSE)
