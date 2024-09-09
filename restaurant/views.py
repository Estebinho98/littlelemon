from rest_framework.decorators import api_view, permission_classes
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, User, UserSerializers
from rest_framework import generics , viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .pagination import Menupagination
from django.shortcuts import render
# Create your views here.



class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = Menupagination

class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = Menupagination



class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Menupagination

def index(request):
    return render(request, 'index.html', {})



@api_view()
@permission_classes([IsAuthenticated])

def msg(request):
    return Response({"message":'This view is protected'})