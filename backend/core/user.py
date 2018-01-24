from django.views.decorators.http import require_POST, require_GET
from django.contrib import auth
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from parse.models import User

