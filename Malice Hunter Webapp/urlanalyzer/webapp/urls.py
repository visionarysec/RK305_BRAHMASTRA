from django.urls import path
from . import views 

urlpatterns = [
    # TODO -> add it back
    # path('',views.home, name='home'),
    path('',views.dashboard, name='dashboard'),
    path('analyze/',views.analyze, name='analyze'),
    path('investigate/',views.investigate, name='investigate'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('blank/',views.blank, name='blank'),
    path('osint/',views.osint, name='osint'),
    path('reports/',views.reports, name='reports'),

]
