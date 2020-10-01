from django.urls import path
from .views import chart_select_view, add_event_view, sales_dist_view

app_name = 'locUnits'

urlpatterns = [
    path('', chart_select_view, name='main-locUnits-view'),
    path('add/', add_event_view, name='add-event-view'),
]
