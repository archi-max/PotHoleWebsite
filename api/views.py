from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from datacollection.models import Data, UploadForm

from .serializers import DataSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden
from rest_framework import generics


class DataViewSet(generics.ListAPIView):

    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.
@csrf_exempt
def UploadData(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        files = request.FILES.getlist("images")
        if form.is_valid():
            username = form.cleaned_data["username"]
            for f in files:
                d = Data(username=username, image=f)
                d.save()
            return HttpResponse("success")
        else:
            return HttpResponse("failed")
    else: return HttpResponseForbidden()