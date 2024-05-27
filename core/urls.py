from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-prediction/<int:fixture_pk>/', views.submit_prediction, name='submit_prediction'),
    path('delete-prediction/<int:prediction_pk>/', views.delete_prediction, name='delete_prediction'),
]
