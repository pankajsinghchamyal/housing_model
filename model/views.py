from django.shortcuts import render
from django.http import HttpResponse
import joblib

# Create your views here.
def home(request):
    return render(request,'home.html')

def predict(request):
    regressor = joblib.load("gbregressor.pkl")
    return HttpResponse('<h1> Result </h1>')
