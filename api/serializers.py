from rest_framework.serializers import ModelSerializer
from .models import Advocate, Company

from rest_framework import serializers    


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'logo', 'name', 'summary', 'href', 'advocate']
        # '__all__'

class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = ['profile_pic', 'username', 'name', 'short_bio', 'long_bio', 'advocate_years_exp', 'company', 'link']

    # def create(self, validated_data):
    #     return Advocate.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.profile_pic = validated_data.get("profile_pic", instance.profile_pic)
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.short_bio = validated_data.get("short_bio", instance.short_bio)
    #     instance.long_bio = validated_data.get("long_bio", instance.long_bio)
    #     instance.advocate_years_exp = validated_data.get("advocate_years_exp", instance.advocate_years_exp)
    #     instance.company = validated_data.get("company", instance.company)
    #     instance.link = validated_data.get("link", instance.link)
    #     instance.created = validated_data.get("created", instance.created)
    #     instance.updated = validated_data.get("updated", instance.updated)
    #     instance.save()
    #     return instance

