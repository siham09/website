from django.contrib import admin
from .models import Temp_Data
from .models import Pulse_Data

admin.site.register(Temp_Data)

admin.site.register(Pulse_Data)