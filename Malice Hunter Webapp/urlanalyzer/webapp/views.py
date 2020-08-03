from django.shortcuts import render
from . import url_detect
from . import red
from .engine import investigate
from django.http import HttpResponse
from django.views.generic import View

from .render_pdf import render_to_pdf

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

def dashboard_analyze(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        # print(url)
        results = url_detect.url_decompress(url)
        print('Results inside view : ')
        print('type :',type(results))
        # print(results)
        for k,v in results['scans'].items() :
            print(k,v)
    else:
        return render(request, 'webapp/analyze.html',{'title':'Analyze'}) 
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
    return render(request, 'webapp/dashboard-analyze.html',{'title':'Analyze','results': data,'pos': pos,'neg': neg,'threats': c1,'safe': c2, 'targetUrl': url})

def dashboard_investigate(request):
    results = dict()
    if request.method == 'POST':
        url = request.POST.get('url')
        # print(url)
        results = url_detect.url_decompress(url)
        #print("Investigated Data :\n",investigate.main(url,"conf.json"))
        #print('Results inside view : ')
        #print('type :',type(results))
        # print(results)
        '''
        for k,v in results['scans'].items() :
            print(k,v)
        '''
        
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
        details = investigate.main(url,"conf.json").all
        print(details)
        print(type(details))
        print(dict(details))
        return render(request, 'webapp/dashboard-investigate.html',{'title':'Investigate','results': data,'pos': pos,'neg': neg,'threats': c1,'safe': c2, 'targetUrl': url, 'details':details})
    
    else:
        return render(request, 'webapp/investigate.html',{'title':'Investigate'}) 
        # data = dict(sorted(results['scans'],key=results['scans']['detected']))


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # data = {
            #  'today': datetime.date.today(), 
            #  'amount': 39.99,
            # 'customer_name': 'Cooper Mann',
            # 'order_id': 1233434,
        # }
        url = request.GET.get('url')
        print(url)
        results = url_detect.url_decompress(url)
        
        print('Results inside view : ')
        print('type :',type(results))
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
        details = investigate.main(url,"conf.json").all
        pdf = render_to_pdf('webapp/report_format.html',{'title':'Analyze','results': data,'pos': pos,'neg': neg,'threats': c1,'safe': c2, 'targetUrl': url, 'details':details})
        return HttpResponse(pdf, content_type='application/pdf')

'''
def OSINT(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        results = red.
'''

def about(request):
    return render(request, 'webapp/page-about.html',{'title':'About'})


def contact(request):
    return render(request, 'webapp/page-contact.html',{'title':'Contact'})


def newFeature(request):
    return render(request, 'webapp/blank.html',{'title':'New Feature'})



    

