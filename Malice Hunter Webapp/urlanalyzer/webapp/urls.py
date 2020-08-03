from django.urls import path
from . import views 

urlpatterns = [
    # TODO -> add it back
    # path('',views.home, name='home'),
    path('',views.dashboard, name='dashboard'),
    path('dashboard-analyze/',views.dashboard_analyze, name='dashboard_analyze'),
    path('investigate/',views.investigate, name='investigate'),
    path('blank/',views.blank, name='blank'),
    path('osint/',views.osint, name='osint'),
    path('reports/',views.reports, name='reports'),
]
