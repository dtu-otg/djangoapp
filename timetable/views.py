from django.shortcuts import render
from django.http import HttpResponse
from .exscript import ttmaker
from rest_framework.generics import GenericAPIView 
from rest_framework.response import Response
from rest_framework import status, permissions
from user.permissions import Authenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .forms import TTForm, SlotForm, TTFormSet
from .models import Course, Slot
from django.forms import inlineformset_factory
from django.urls import reverse

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

class CourseListView(ListView):
    model = Course 

class TTFormView(CreateView):
    model = Course 
    fields = ['code', 'name', 'islab', 'group', 'batch', 'prof_name', 'prof_mail']

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["slots"] = TTFormSet(self.request.POST)
        else:
            data["slots"] = TTFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        slots = context["slots"]
        self.object = form.save()
        if slots.is_valid():
            slots.instance = self.object
            slots.save()
        return super().form_valid(form)

    def get_success_url(self):
        # return HttpResponse("<h1>Thanks!</h1>")
        return reverse("ttlist")

# Create your views here.

year_param = openapi.Parameter('year', openapi.IN_QUERY, description="year for time table e.g. 2k19", type=openapi.TYPE_STRING)
batchgrp_param = openapi.Parameter('batchgrp', openapi.IN_QUERY, description="batch group time table e.g. A / B", type=openapi.TYPE_STRING)
batchnum_param = openapi.Parameter('batchnum', openapi.IN_QUERY, description="batch number for time table e.g 1, 2, 3, etc", type=openapi.TYPE_INTEGER)

# class TimeTableView(GenericAPIView):
#     # permission_classes = [Authenticated]

#     @swagger_auto_schema(operation_description="get timetable", manual_parameters=[year_param, batchgrp_param, batchnum_param])
#     def get(self, request):
#         year = request.GET["year"]
#         batchgrp = request.GET["batchgrp"]
#         batchnum_s = request.GET["batchnum"]
#         try:
#             batchnum = int(batchnum_s)
#         except e:
#             response = HttpResponse('')
#             response.status_code = 69
#             return response
#         tt = ttmaker(year, batchgrp, batchnum, True)
#         return Response(tt, status=status.HTTP_200_OK)

# def TTFormView(request):
#     if request.method == 'GET':
#         form = TTForm()
#         # TTFormSet = inlineformset_factory(Course, Slot, fields=('day', 'time'), extra=5)
#         return render(request, 'timetable/form.html', {'form':form, 'formset': TTFormSet})
#     else:
#         form = TTFormSet(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.course.save()
#             form.save()
#             return HttpResponse("<h1>Thanks!</h1>")
#         return HttpResponse("<h1>Error!</h1>")



