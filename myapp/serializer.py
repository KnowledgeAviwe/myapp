#from myapi.myapp.models import FoodTable
from rest_framework import serializers
from .models import FoodTable

class FoodTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodTable
        fields= '__all__'