#!/usr/bin/env python
# coding: utf-8
import os
import sys
from django.conf import settings
from django.core.management import call_command



conf = dict(
    INSTALLED_APPS = ['autoslug'],
    DATABASES = dict(
        default = dict(
            ENGINE='django.db.backends.sqlite3',
        ),
    ),
    AUTOSLUG_SLUGIFY_FUNCTION = 'django.template.defaultfilters.slugify',
)


settings.configure(**conf)


if __name__ == "__main__":
    call_command('test', 'autoslug')
