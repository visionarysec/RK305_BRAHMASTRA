from django.shortcuts import render
from . import url_detect

url = ""
# Create your views here.
#TODO -> add home back -> <!-- <li><a href="{% url 'home' %}">Home</a></li> -->
# def home(request):
#     return render(request, 'webapp/index.html',{'title':'Home'})
#

# adding dashboard
def dashboard(request):
    return render(request, 'webapp/dashboard.html',{'title':'Dashboard'})

def analyze(request):
    return render(request, 'webapp/page-seo-analysis.html',{'title':'Analyze'})

import json

def investigate(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        # print(url)
        results = url_detect.url_detect(url)
        print('Results inside view : ')
        print('type :',type(results))
        # print(results)
        for k,v in results['scans'].items() :
            print(k,v)
    # data = dict(sorted(results['scans'],key=results['scans']['detected']))
    data = results['scans']
    pos = dict()
    neg = dict()

    for k,v in data.items():
        if v['detected'] == True:
            neg[k] = v
        else:
            pos[k] = v
    
    c1 = len(neg)
    c2 = len(pos)
    return render(request, 'webapp/dashboard-investigate.html',{'title':'Investigate','results': data,'pos': pos,'neg': neg,'threats': c1,'safe': c2})


def about(request):
    return render(request, 'webapp/page-about.html',{'title':'About'})


def contact(request):
    return render(request, 'webapp/page-contact.html',{'title':'Contact'})


def newFeature(request):
    return render(request, 'webapp/blank.html',{'title':'New Feature'})

