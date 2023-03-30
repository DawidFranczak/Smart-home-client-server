#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import threading
from aquarium.api.thread import aquas_check
from temperature.api.thread import tempCheck
from listener.thread import listener


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smart_home_client.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    threading.Thread(target=listener).start()
    threading.Thread(target=aquas_check, daemon=True).start()
    threading.Thread(target=tempCheck, daemon=True).start()

    main()
