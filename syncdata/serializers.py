from rest_framework import serializers
from .models import AccMaster, AccProduct, AccProductBatch, AccUsers, Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class AccMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccMaster
        fields = '__all__'


class AccProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccProduct
        fields = '__all__'


class AccProductBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccProductBatch
        fields = '__all__'


class AccUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccUsers
        fields = ['id', 'pass_field', 'role', 'client_id']
