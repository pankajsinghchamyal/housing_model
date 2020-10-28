from django.shortcuts import render
from django.http import HttpResponse
# import joblib
# import numpy as np

# Create your views here.
def home(request):
    return render(request,'home.html')

def predict(request):
    # regressor = joblib.load("gbregressor.pkl")
    l = []
    d = dict()
    def extract_value(key):
        l.append(float(request.POST[key]))
        d[key] = request.POST[key]
    cols = ['bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']
    if(request.method == 'POST'):
        for key in cols:
            extract_value(key)
    
        

    # l =  [3,1,1180,5650,1,0,0,3,7,1180,0,1955,0,98178,47.5112,-122.257,1340,5650]
    # l = np.array(l)
    # l = np.reshape(l,(1,l.shape[0]))
    
    # res =  regressor.predict(l)
    # d['res'] = res
    return render(request,"result.html",d)
    # return HttpResponse("yes")
