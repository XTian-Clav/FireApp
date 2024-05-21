from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, IncidentList, IncidentCreateView, IncidentUpdateView, IncidentDeleteView
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),

    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('pieChart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('stations', views.map_station, name='map-station'),
    path('incidents', views.fire_incidents, name='fire-incidents'),

    path('list', IncidentList.as_view(), name='firestation-list'),
    path('list/add', IncidentCreateView.as_view(), name='firestation-add'),
    path('list/<pk>', IncidentUpdateView.as_view(), name='firestation-update'),
    path('list/<pk>/delete', IncidentDeleteView.as_view(), name='firestation-delete'),
]
