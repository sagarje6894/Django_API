from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Flight_details
from .serilizers import FlightDetailsser


# Create your views here.
class Flight(APIView):
    def get(self,r):
        flightdetails = Flight_details.objects.all()
        serobj = FlightDetailsser(flightdetails,many=True)
        return Response(serobj.data)

    def post(self,r):
        serobj = FlightDetailsser(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)


class FlightUpdateDelete(APIView):
    def put(self,r,pk):
        flightobj = Flight_details.objects.get(pk=pk) ##data from databse
        serobj = FlightDetailsser(flightobj,data=r.data) ##data from user
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        flightobj = Flight_details.objects.get(pk=pk)
        flightobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
