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
    if(request.method == 'POST'):
        l.append(request.POST['bedrooms'])
        l.append(request.POST['bathrooms'])
        l.append(request.POST['sqft_living'])
        l.append(request.POST['sqft_lot'])
        l.append(request.POST['floors'])
        l.append(request.POST['waterfront'])
        l.append(request.POST['view'])
        l.append(request.POST['condition'])
        l.append(request.POST['grade'])
        l.append(request.POST['sqft_above'])
        l.append(request.POST['sqft_basement'])
        l.append(request.POST['yr_built'])
        l.append(request.POST['yr_renovated'])
        l.append(request.POST['zipcode'])
        l.append(request.POST['lat'])
        l.append(request.POST['long'])
        l.append(request.POST['sqft_living15'])
        l.append(request.POST['sqft_lot15'])
        

    # l =  [3,1,1180,5650,1,0,0,3,7,1180,0,1955,0,98178,47.5112,-122.257,1340,5650]
    l = np.array(l)
    l = np.reshape(l,(1,l.shape[0]))
    print("result:    " ,regressor.predict(l))
    res = regressor.predict(l)
    return HttpResponse(str(res))
