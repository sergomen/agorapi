from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from django.db.models import Q

@api_view(['GET'])
def endpoints(request):
    
    routes = ['/advocates/', '/advocates/:username/',
              '/companies/', '/companies/:id/',
              '/advocates/?query=username', '/advocates/?page=number']

    return Response(routes)

@api_view(['GET', 'POST'])
def getAdvocates(request):
	
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''
        paginator = PageNumberPagination()
        
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(long_bio__icontains=query))
        p = paginator.paginate_queryset(queryset=advocates, request=request)
        serializer = AdvocateSerializer(p, many=True)
        return paginator.get_paginated_response({"advocates": serializer.data})

    if request.method == 'POST':
        data = request.data
        advocate = Advocate.objects.create(
                username = data['username'],
                name = data['name'],
                short_bio = data['short_bio'],
                long_bio = data['long_bio'],
                advocate_years_exp = data['advocate_years_exp'],
                link = data['link']
        )
        advocate.company.set(data['company'])
        serializer = AdvocateSerializer(advocate, many=False)
        return Response({"advocate": serializer.data})


@api_view(['GET', 'PUT', 'DELETE'])
def getAdvocate(request, username):
    advocate = ''
    try:
        advocate = Advocate.objects.get(username=username)
    except:
        return Response('User does not exist')

    if request.method == 'GET':
        serializer = AdvocateSerializer(advocate, many=False)
        return Response({"advocate": serializer.data})

    if request.method == 'PUT':
        advocate.username = request.data['username']
        advocate.name = request.data['name']
        advocate.short_bio = request.data['short_bio']
        advocate.long_bio = request.data['long_bio']
        advocate.advocate_years_exp = request.data['advocate_years_exp']
        advocate.link = request.data['link']
        advocate.company.set(request.data['company'])
        serializer = AdvocateSerializer(advocate, many=False)
    if serializer.is_valid():
        serializer.save()

        return Response({"advocate": serializer.data})

    if request.method == 'DELETE':
        advocate.delete()
        return Response('Advocate was deleted!')

# /////////////////////////////////////////////////

# class AdvocateAPIListPagination(PageNumberPagination):
# 		page_size = 10
# 		page_size_query_param = 'page.size'
# 		max_page_size = 100

class CompanyAPIListPagination(PageNumberPagination):
		page_size = 1
		page_size_query_param = 'page.size'
		max_page_size = 1

# ///////////////////////////////////////// 

class CompanyAPIList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = CompanyAPIListPagination

class CompanyAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
