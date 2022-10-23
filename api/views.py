from django.http import JsonResponse
from django.shortcuts import render

from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from django.db.models import Q

@api_view(['GET'])
def endpoints(request):
    
    routes = ['/advocates/', '/advocates/:username/',
              '/companies/', '/companies/:name/',
              '/advocates/?query=username', '/companies/?query=name']

    return Response(routes)

@api_view(['GET', 'POST'])
def getAdvocates(request):
	
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(long_bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

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
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def getAdvocate(request, username):
    advocate = ''
    try:
        advocate = Advocate.objects.get(username=username)
    except:
        return Response('User does not exist')

    if request.method == 'GET':
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

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

        return Response(serializer.data)

    if request.method == 'DELETE':
        advocate.delete()
        return Response('Advocate was deleted!')

class AdvocateViewSet(viewsets.ModelViewSet):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer

    def get_queryset(self):
        return Advocate.objects.all()[:4]

    @action(methods=['get'], detail=False)
    def username(self, request):
        usernames = Advocate.objects.get(id)
        return Response({'usernames':[c.username for c in usernames]})

# /////////////////////////////////////////////////

class AdvocateAPIListPagination(PageNumberPagination):
		page_size = 10
		page_size_query_param = 'page.size'
		max_page_size = 1000

class CompanyAPIListPagination(PageNumberPagination):
		page_size = 10
		page_size_query_param = 'page.size'
		max_page_size = 1000

# ///////////////////////////////////////////////
@api_view(['GET'])
def advocates(request):
		query = request.GET.get('query')
		
		if query == None:
				query = ''

		advocates = Advocate.objects.filter(username__icontains=query)
		serializer = AdvocateSerializer(advocates, many=True)
		return Response(serializer.data)

class AdvocateAPIList(generics.ListCreateAPIView):
    def get(self, request):
        query = request.GET.get('query')
        
        if query == None:
                query = ''
        
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(short_bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response({'advocates': serializer.data})

    
    # queryset = Advocate.objects.all()
    # serializer_class = AdvocateSerializer
    # pagination_class = AdvocateAPIListPagination

class AdvocateAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer

# /////////////////////////////////////////

class CompanyAPIList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = CompanyAPIListPagination

class CompanyAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# class AdvocateAPIView(APIView):
#     def get(self, request):
#         advocates = Advocate.objects.all()
#         return Response({'advocates': AdvocateSerializer(advocates, many=True).data})

#     def post(self, request):
#         serializer = AdvocateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True) # if true -> validated_data
#         serializer.save()
#         return Response({'advocate': serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = Advocate.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})

#         serializer = AdvocateSerializer(data=request.data, instance=instance)
#         serializer.is_valid()
#         serializer.save()
#         return Response({"advocate": serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = Advocate.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})

#         serializer = AdvocateSerializer(data=request.data, instance=instance)
#         serializer.is_valid()
#         serializer.delete()
#         return Response({"advocate": serializer.data})

# @api_view(['GET'])
# def getAdvocates(request):
#     advocates = Advocate.objects.all()
#     serializer = AdvocateSerializer(advocates, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getAdvocate(request, pk):
#     advocate = Advocate.objects.get(id=pk)
#     serializer = AdvocateSerializer(advocate, many=False)
#     return Response(serializer.data)

# class CompanyAPIView(APIView):
#     def get(self, request):
#         companies = Company.objects.all()
#         return Response({'companies': AdvocateSerializer(companies, many=True).data})

# @api_view(['GET'])
# def getCompanies(request):
#     companies = Company.objects.all()
#     serializer = CompanySerializer(companies, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getCompany(request, pk):
#     company = Company.objects.get(id=pk)
#     serializer = CompanySerializer(company, many=False)
#     return Response(serializer.data)