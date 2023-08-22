from rest_framework import serializers
from .models import *

class SampleIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleIntake
        fields = '__all__'