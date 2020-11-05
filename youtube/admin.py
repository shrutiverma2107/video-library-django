from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

admin.site.register(Videos)