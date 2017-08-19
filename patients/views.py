# from django.shortcuts import get_object_or_404
from django.db.models import Model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Temp_Data
from .serializers import Temp_DataSerializer
from .models import Pulse_Data
from .serializers import Pulse_DataSerializer
from django.http import Http404
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to T2HM</h1>")

# Lists all Temp_Data or create a new one
# temp_data/
class Temp_DataList(APIView):

    def get(self, request):
        temp_datas = Temp_Data.objects.all()
        serializer = Temp_DataSerializer(temp_datas, many=True)
        return Response(serializer.data)

    def post(self, request):
#        serializer = Temp_DataSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(request.data)
# Lists all Pulse_Data or create a new one
# pulse_data/
class Pulse_DataList(APIView):

    def get(self, request):
        pulse_datas = Pulse_Data.objects.all()
        serializer = Pulse_DataSerializer(pulse_datas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Pulse_DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Temp_DataDetail(APIView):
    def get_object(self, pk):
        try:
            return Temp_Data.objects.get(pk=pk)
        except Temp_Data.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = Temp_DataSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = Temp_DataSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Pulse_DataDetail(APIView):
    def get_object(self, pk):
        try:
            return Pulse_Data.objects.get(pk=pk)
        except Pulse_Data.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = Pulse_DataSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = Pulse_DataSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

