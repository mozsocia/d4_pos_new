from django.shortcuts import render
from django.views import View
from ..serializers import *
from ..models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from pprint import pprint
from django.db import transaction

# Create your views here.


def hello_view(request):
    message = "Hello World Django"
    return render(request, 'firstapp/hello.html', {'message': message})

def test_view(request):
    return render(request, 'firstapp/test.html')