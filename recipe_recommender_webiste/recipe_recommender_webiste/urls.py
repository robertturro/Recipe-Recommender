from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recommender_app/', include('recommender_app.urls'))
    
]
