#!/usr/bin/env python
"""
Command-line utility for administrative tasks.

# For more information about this file, visit
# https://docs.djangoproject.com/en/2.1/ref/django-admin/
"""

import os
import sys

if __name__ == '__main__':
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'DWBIProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


  

#if __name__ == '__main__':
#    # Get the desired port number
#    port = 63343

#    # Update the environment variable to use the desired port
#    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DWBIProject.settings')
#    os.environ["RUN_MAIN"] = "true"
#    os.environ["PORT"] = str(port)

#    try:
#        from django.core.management import execute_from_command_line
#    except ImportError as exc:
#        raise ImportError("Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?") from exc

#    # Start the development server with the specified port
#    execute_from_command_line(['manage.py', 'runserver', f'localhost:{port}'])

