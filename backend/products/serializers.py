from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'price', 'description', 'stock_count')
        # fields = '__all__' - anti practice
        # exclude = ('id',)
