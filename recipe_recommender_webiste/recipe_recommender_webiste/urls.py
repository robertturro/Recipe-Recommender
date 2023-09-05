from django.contrib import admin
from django.urls import path
from . import views

app_name = "recommender_app"


urlpatterns = [
    path('admin/', admin.site.urls),
    
]
