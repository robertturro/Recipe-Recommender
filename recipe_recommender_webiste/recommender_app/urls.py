from django.urls import path, include 
from . import views

app_name = "recommender_app"

urlpatterns = [ 
    
    path('signup/', views.signup, name='signup'),
    path("accounts/", include("django.contrib.auth.urls")),

    path('dashboard/', views.dashboard, name = 'dash'),
    path('recommend/', views.recommend, name="rec"),
    path('results/', views.results, name="results"),
    path('new_user/', views.first_time_dashboard, name="new_user"),
    path('liked_recipes/',views.liked_recipes,name="liked_recipes"),

    path('upload_data/', views.import_from_excel, name='upload')
] 
