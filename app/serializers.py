from rest_framework import serializers

from app.models import *

class Product_CategoryData(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'