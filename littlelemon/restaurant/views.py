from django.shortcuts import render 
from django.http import HttpResponse
from rest_framework import generics
from .models import Menu,Booking
from .serializers import BookingSerializers,MenuSerializers,UserSerializer
from rest_framework import permissions, viewsets,routers
from django.contrib.auth.models import User

# View function to print Hello.
def index(request):
    return render(request, 'index.html', {})
#Adding MenuItemView class
class MenuItemsView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializers
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializers
class BookingViewset(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializers
    