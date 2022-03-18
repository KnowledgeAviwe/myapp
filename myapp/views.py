from django.shortcuts import render
from  rest_framework.views import APIView
from rest_framework.response import  Response
from .serializer import FoodTableSerializer
from .models import FoodTable

# Create your views here.
class FoodList(APIView):
    def get(self,request):
        food = FoodTable.objects.all()
        query = self.request.GET.get('search')
        if query is not None:
            food=food.filter(name__contains=query)| food.filter(shop__contains=query)
        serializer= FoodTableSerializer(food,many=True)
        return Response(serializer.data)
