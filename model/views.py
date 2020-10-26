from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np

# Create your views here.
def home(request):
    return render(request,'home.html')

def predict(request):
    regressor = joblib.load("gbregressor.pkl")
    l = []
    feature = []
    def extract_value(key):
        l.append(float(request.POST[key]))
        feature.append(request.POST[key])
    cols = ['bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']
    if(request.method == 'POST'):
        for key in cols:
            extract_value(key)
        # l.append(float(request.POST['bedrooms']))
        # l.append(float(request.POST['bathrooms']))
        # l.append(float(request.POST['sqft_living']))
        # l.append(float(request.POST['sqft_lot']))
        # l.append(float(request.POST['floors']))
        # l.append(float(request.POST['waterfront']))
        # l.append(float(request.POST['view']))
        # l.append(float(request.POST['condition']))
        # l.append(float(request.POST['grade']))
        # l.append(float(request.POST['sqft_above']))
        # l.append(float(request.POST['sqft_basement']))
        # l.append(float(request.POST['yr_built']))
        # l.append(float(request.POST['yr_renovated']))
        # l.append(float(request.POST['zipcode']))
        # l.append(float(request.POST['lat']))
        # l.append(float(request.POST['long']))
        # l.append(float(request.POST['sqft_living15']))
        # l.append(float(request.POST['sqft_lot15']))
        

    # l =  [3,1,1180,5650,1,0,0,3,7,1180,0,1955,0,98178,47.5112,-122.257,1340,5650]
    l = np.array(l)
    l = np.reshape(l,(1,l.shape[0]))
    
    res =  regressor.predict(l)
    return render(request,"result.html",{'feature':feature,"res":res})
