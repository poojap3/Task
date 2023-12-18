from django.shortcuts import render
from .serializers import *
from .models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

#FOR CREATING APIs

class TaskAPIView(APIView):

#to get all the Task
    def get(self, request):

        id =self.request.query_params.get('id')
        if id:
            profile = Task.objects.filter(id=id).values()
            return Response(profile)
        else:

            profile = Task.objects.all().values()
            return Response(profile)

#to post the Task
    def post(self, request):
        data = request.data

        name = data.get('name')
        discription= data.get('discription')

        jobcreate = Task.objects.create(name= name, discription=discription )
        return Response("Data Added Sucessfully")


#to edit the Task
    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Task.objects.filter(id=id).update(name = data.get('name'),discription=data.get('discription'))

            if data:
                    return JsonResponse({'message': 'data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)



        else:
            return JsonResponse({'message': 'Id Required.'})

#to delete the Task
    def delete(self, request):


        id =self.request.query_params.get('id')
        item = Task.objects.filter(id= id)

        if len(item) > 0:
            item.delete()
            return Response("Item Deleted Sucessfully")
        else:
            return Response("Id Required.")
