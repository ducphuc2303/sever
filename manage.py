# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()
# '''
# admin/
# api/ openapi.json [name='openapi-json']
# api/ docs [name='openapi-view']
# api/ books [name='list_books']
# api/ books [name='create_book']
# api/ books/<id> [name='get_book']
# api/ books/<id> [name='update_book']
# api/ books/<id> [name='delete_book']
# api/ users [name='list_users']
# api/ [name='api-root']
# '''
"""
WSGI config for rest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')

application = get_wsgi_application()