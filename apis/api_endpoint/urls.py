
from django.urls import path
from home import views

urlpatterns = [
    path('get-client/', views.get_info),
    path('client/',views.clientapi.as_view())
]