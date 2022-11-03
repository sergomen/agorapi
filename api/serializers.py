from rest_framework.serializers import ModelSerializer
from .models import Advocate, Company  


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'logo', 'name', 'summary', 'href', 'advocate']


class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = ['profile_pic', 'username', 'name', 'short_bio', 'long_bio', 'advocate_years_exp', 'company', 'link']
