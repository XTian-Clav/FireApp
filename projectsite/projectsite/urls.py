from django.contrib import admin
from django.urls import path

from fire.views import (
    HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, map_station, fire_incidents,
    
    LocationsList, LocationsCreateView, LocationsUpdateView, LocationsDeleteView,
    FirestationList, FirestationCreateView, FirestationUpdateView, FirestationDeleteView,
    IncidentList, IncidentCreateView, IncidentUpdateView, IncidentDeleteView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),

    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('pieChart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('stations', map_station, name='map-station'),
    path('incidents', fire_incidents, name='fire-incidents'),

    path('locations_list', LocationsList.as_view(), name='locations-list'),
    path('locations_list/add/', LocationsCreateView.as_view(), name='locations-add'),
    path('locations_list/<pk>', LocationsUpdateView.as_view(), name='locations-update'),
    path('locations_list/<pk>/delete', LocationsDeleteView.as_view(), name='locations-delete'),

    path('incident_list', IncidentList.as_view(), name='incident-list'),
    path('incident_list/add/', IncidentCreateView.as_view(), name='incident-add'),
    path('incident_list/<pk>', IncidentUpdateView.as_view(), name='incident-update'),
    path('incident_list/<pk>/delete', IncidentDeleteView.as_view(), name='incident-delete'),

    path('firestation_list', FirestationList.as_view(), name='firestation-list'),
    path('firestation_list/add/', FirestationCreateView.as_view(), name='firestation-add'),
    path('firestation_list/<pk>', FirestationUpdateView.as_view(), name='firestation-update'),
    path('firestation_list/<pk>/delete', FirestationDeleteView.as_view(), name='firestation-delete'),
]
