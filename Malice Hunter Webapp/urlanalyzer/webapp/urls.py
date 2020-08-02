from django.urls import path
from . import views 

urlpatterns = [
    # TODO -> add it back
    # path('',views.home, name='home'),
    path('',views.dashboard, name='dashboard'),
    path('analyze/',views.analyze, name='analyze'),
    path('dashboard-analyze/',views.dashboard_analyze, name='dashboard_analyze'),
    path('investigate/',views.investigate, name='investigate'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('blank/',views.newFeature, name='blank')
    
]