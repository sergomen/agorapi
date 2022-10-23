from django.urls import path, include
from . import views
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'advocates', views.AdvocateViewSet)


urlpatterns = [
    path('', views.endpoints),
    # path('', include(router.urls)), #http://127.0.0.1:8000/api/v1/advocates/
    path('advocates/', views.getAdvocates, name="advocates"),
    path('advocates/<str:username>/', views.getAdvocate, name="advocate"),
    # path('advocates/<int:pk>/', views.AdvocateAPIDetailView.as_view(), name="advocate"),

    # path('advocates/', views.AdvocateViewSet.as_view({'get': 'list'}), name="advocates"),
    # path('advocates/<int:pk>/', views.AdvocateViewSet.as_view({'put': 'update'}), name="advocate"),
    

    # path('advocates/<str:pk>/', views.getAdvocate, name="advocate"),

    path('companies/', views.CompanyAPIList.as_view(), name="companies"),
    path('companies/<int:pk>/', views.CompanyAPIDetailView.as_view(), name="company"),
    
    # path('companies/<str:pk>/', views.getCompany, name="company"),
]