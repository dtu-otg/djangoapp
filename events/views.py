from rest_framework import generics,status,permissions,views,response,mixins
from user.permissions import *
from .models import Event,RegistrationEvent
from django.db.models import Q
from .serializers import *
from user.models import User
from rest_framework.parsers import MultiPartParser,FormParser


class GetEventsView(generics.ListAPIView):
    serializer_class = GetEventsSerializer
    permission_classes = [AuthenticatedActivated]

    def get_queryset(self):
        uni = self.request.GET.get('university',None)
        society = self.request.GET.get('society',None)
        social = self.request.GET.get('social',None)
        qs = Event.objects.all()
        q = Q()
        if uni != None:
            q |= Q(type_list = '1')
        if society != None:
            q |= Q(type_list = '2')
        if social != None:
            q |= Q(type_list = '3')
        return qs.filter(q).order_by('date_time')

    def get_serializer_context(self,**kwargs):
        data = super().get_serializer_context(**kwargs)
        data['user'] = self.request.user.username
        return data
        

class RegisterForEventView(generics.GenericAPIView):
    permission_classes = [AuthenticatedActivated]
    serializer_class = RegistrationEventSerializer

    def post(self,request,*args, **kwargs):
        data = request.data
        username = data.get('username',None)
        event_id = data.get('event_id',None)
        if username is None:
            return response.Response({"status" : 'FAILED','error' :"Username has not been provided"},status=status.HTTP_400_BAD_REQUEST)
        if event_id is None:
            return response.Response({"status" : 'FAILED','error' :"Event_id has not been provided"},status=status.HTTP_400_BAD_REQUEST) 
        user = User.objects.get(username=username)
        event = Event.objects.get(id=event_id)
        if RegistrationEvent.objects.filter(user=user,event=event).exists():
            return response.Response({"status" : 'FAILED','error' :"You are already registered"},status=status.HTTP_400_BAD_REQUEST)
        RegistrationEvent.objects.create(user=user,event=event)
        return response.Response({'status' : 'OK','result' :'Registration for the given event for the given user has been saved'},status=status.HTTP_200_OK)

class UnRegisterForEventView(generics.GenericAPIView):
    permission_classes = [AuthenticatedActivated]
    serializer_class = RegistrationEventSerializer

    def post(self,request,*args, **kwargs):
        data = request.data
        username = data.get('username',None)
        event_id = data.get('event_id',None)
        if username is None:
            return response.Response({"status" : 'FAILED','error' :"Username has not been provided"},status=status.HTTP_400_BAD_REQUEST)
        if event_id is None:
            return response.Response({"status" : 'FAILED','error' :"Event_id has not been provided"},status=status.HTTP_400_BAD_REQUEST) 
        user = User.objects.get(username=username)
        event = Event.objects.get(id=event_id)
        if RegistrationEvent.objects.filter(user=user,event=event).exists():
            RegistrationEvent.objects.filter(user=user,event=event).delete()
            return response.Response({"status" : 'OK','error' :"You have been unregistered"},status=status.HTTP_200_OK)
        return response.Response({'status' : 'Failed','result' :'You did not register for this event'},status=status.HTTP_400_BAD_REQUEST)

class CreateEventView(generics.CreateAPIView):
    permission_classes = [Hosting]
    parser_classes = [MultiPartParser,FormParser]
    serializer_class = CreateEventSerializer

    def get_serializer_context(self,**kwargs):
        data = super().get_serializer_context(**kwargs)
        data['user'] = self.request.user.username
        return data

    def post(self,request):
        data = request.data
        serializer = CreateEventSerializer(data=data)
        if serializer.is_valid():
            return response.Response({"status" : 'OK','result' :"New event created"},status=status.HTTP_200_OK)
        return response.Response(serializer.errors)

class EventDetailsView(generics.RetrieveAPIView):
    permission_classes = [AuthenticatedActivated]
    serializer_class = EventDetailserializer
    queryset = Event.objects.all()
    lookup_field = 'id'

    def get_serializer_context(self,**kwargs):
        data = super().get_serializer_context(**kwargs)
        data['user'] = self.request.user.username
        return data
