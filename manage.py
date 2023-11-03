#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TMS_Pro.development_settings')
    if os.getenv("DJANGO_SETTINGS_MODULE") is None:
        print(""" 
        Warning: django is running in development mode by default. If you are deploying this application you must set the environment variable:

        DJANGO_SETTINGS_MODULE to 'TMS_Pro.production_settings'

        Alternatively, if you're running in development mode intentionally, you can quiet this message by setting:

        DJANGO_SETTINGS_MODULE to 'TMS_Pro.development_settings'
        """)

    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
