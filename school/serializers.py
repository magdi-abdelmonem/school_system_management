from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *


class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=subject
        fields=['sub_name','chapter']


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['pk','name','subject']


class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=teacher
        fields=['pk','name','subject']