from django.shortcuts import render  # noqa
from django.http import HttpResponse

from currency.utils import get_password


def generate_password(request):
    password = get_password()
    return HttpResponse(password)
