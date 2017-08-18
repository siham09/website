from rest_framework import serializers
from .models import Temp_Data
from .models import Pulse_Data

class Temp_DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Temp_Data
#        fields = ('ticker', 'times')
        fields = '__all__'

class Pulse_DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pulse_Data
#        fields = ('ticker', 'times')
        fields = '__all__'