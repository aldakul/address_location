from datetime import datetime
from django.core.exceptions import ValidationError

import requests


def send_get(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers)
    return response
