from rest_framework import serializers
from .models import Testm


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testm
        fields = '__all__'