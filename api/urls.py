from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.getAdvocates, name="advocates"),
    path('advocates/<str:username>/', views.getAdvocate, name="advocate"),

    path('companies/', views.CompanyAPIList.as_view(), name="companies"),
    path('companies/<str:name>/', views.CompanyAPIDetailView.as_view(), name="company"),
]