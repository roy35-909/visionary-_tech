from django.db import transaction
from rest_framework import serializers

from products.models import Product, ProductMedia, ProductPrice


class ProductSerializer(serializers.ModelSerializer):

    """ serializer """
    product_media = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('id', 'store', 'category', 'name', 'description', 'sku', 'upc', 'discount', 'available',
                  'star_rating', 'likes', 'detail_desc', 'is_active', 'created_by', 'created_at', 'updated_by',
                  'updated_at','product_media','product_price')
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_by', 'updated_at',)


    def get_product_media(self,obj):
        
        medias = ProductMedia.objects.filter(product=obj.id)
        request = self.context.get('request')
        medias_serializerr = ProductMediaSerializerForProductList(medias,many=True,context = {'request':request})
        return medias_serializerr.data
    
    def get_product_price(self,obj):
        try:
            price = ProductPrice.objects.get(product = obj.id)
            price_serializer = ProductPriceSerializerForProductList(price,many=False)
            return price_serializer.data
        except:
            return None
    
class ProductPriceSerializerForProductList(serializers.ModelSerializer):

    class Meta:
        model = ProductPrice
        fields = ('id','quantity_min', 'quantity_max', 'price', 'delivery_time', 'time_unit', 'discount_price')

class ProductMediaSerializerForProductList(serializers.ModelSerializer):

    class Meta:
        model = ProductMedia
        fields = ('id', 'product', 'media', 'display_order', 'is_active')

class ProductPriceSerializer(serializers.ModelSerializer):

    """ serializer """

    class Meta:
        model = ProductPrice
        fields = ('id', 'product', 'quantity_min', 'quantity_max', 'price', 'delivery_time', 'time_unit', 'discount_price', 'is_active',
                  'created_by', 'created_at', 'updated_by', 'updated_at',)
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_by', 'updated_at',)


class ProductMediaSerializer(serializers.ModelSerializer):

    """ serializer """

    class Meta:
        model = ProductMedia
        fields = ('id', 'product', 'media', 'display_order', 'is_active', 'created_by', 'created_at', 'updated_by', 'updated_at',)
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_by', 'updated_at',)
