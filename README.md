# Temii

[![Join the chat at https://gitter.im/DjangoQuilla/temii](https://badges.gitter.im/DjangoQuilla/temii.svg)](https://gitter.im/DjangoQuilla/temii?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/DjangoQuilla/temii.svg?branch=master)](https://travis-ci.org/DjangoQuilla/temii)

Aplicación para escoger los futuros temas y talleristas para las charlas de la comunidad Django Barranquilla.

### Requerimientos

 * [Python 2.7.x](https://www.python.org/)  
 * [PIP](https://pypi.python.org/pypi/pip)
 * [Virtualenv + VirtualenWrapper](https://pypi.python.org/pypi/virtualenv)
 * [Django 1.8.7](https://www.djangoproject.com/)
 * Editor de texto (Sublime Text, Atom, etc)

### Contribuciones

Necesitamos de tu ayuda para terminar este proyecto! **¿Cómo puedes contribuir?** Mira las normas que hemos redactado en el archivo [CONTRIBUTING.md] para organizarnos mejor en el desarrollo. Esperamos tus Pull Requests e Issues. Gracias por tu apoyo.

Agradecimientos a los [autores](AUTHORS.md) de temii

[CONTRIBUTING.md]: https://github.com/DjangoQuilla/temii/blob/master/CONTRIBUTING.md

##### Licencia

[Apache License 2.0](LICENSE)

### Scripts

Instalación de dependencias
: pip install -r requirements/local.txt

Minimizar assets
: python manage.py assets build --manifest django

Recolección de estaticos
: python manage.py collectstatic

Correr servidor
: python manage.py runserver
