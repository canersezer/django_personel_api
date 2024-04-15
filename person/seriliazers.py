from django.utils import timezone

from rest_framework import serializers

from .models import Person,Departman

class CustomDateField(serializers.ReadOnlyField):
    def to_representation(self, value):
        return value.date()


class PersonSerializer(serializers.ModelSerializer):
    start_date = CustomDateField()
    #date = serializers.SerializerMethodField()
    class Meta():
        model = Person
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        user = self.context['request'].user
        personel = Person.objects.create(user=user, **validated_data)
        return personel
    


class DepartmanSerializer(serializers.ModelSerializer):
    person_count = serializers.SerializerMethodField()
    class Meta():
        model = Departman
        fields = '__all__'
        read_only_fields = ['id','name','person_count']
    
    def get_person_count(self,obj):
        return obj.person_set.count()
      
    
    



