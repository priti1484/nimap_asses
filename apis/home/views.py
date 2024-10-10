from django.shortcuts import render
from .models import Client
from rest_framework.response import Response
from .serializers import ClientSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.


@api_view()
def get_info(request):
    queryset = Client.objects.all()
    serializer = ClientSerializer(queryset,many=True)

    return Response({
        "data" : serializer.data
    })

class clientapi(APIView):
    def get(self,request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset,many=True)
        return Response({
            "data": serializer.data
        })

    def post(self, request):
        data= request.data
        serializer= ClientSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "message": "data not saved",
                "errors": serializer.errors,

            })
        serializer.save()
        return Response({
            "message": "data saved"

        })


    def patch(self, request):
        data = request.data
        if not data.get('id'):
            return Response({
                "message":"data not updated",
                "errors": "id is required",
            })
        client=Client.objects.get(id= data.get('id'))
        serializer = ClientSerializer(client,data=data,partial=True)
        if not serializer.is_valid():
            return Response({
                "message": "data not saved",
                "errors": serializer.errors,
            })
        serializer.save()
        return Response({
            "message": "data saved"
        })


    def delete(self, request):
        data = request.data
        if not data.get('id'):
            return Response({
                "message": "data not updated",
                "errors": "id is required",
            })
        client= Client.objects.get(id= data.get('id')).delete()
        return Response({
            "message": "data deleted",
            "data": {}

        })
