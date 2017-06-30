#!/usr/bin/env python
import os
import sys

import dotenv

if __name__ == "__main__":
    #dotenv.read_dotenv()
    if os.getenv('PRODUCTION'):
        dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), './production.env'))
    elif os.getenv('LOCALHOST'):
        dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), './local.env'))
    else:
        dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), './development.env'))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "towan.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
