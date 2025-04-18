from rest_framework import serializers
from .models import Users, Order, OrderClosure, Accounting


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'full_name', 'status']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['qayerdan', 'qayerga', 'client', 'price', 'description']


class OrderClosureSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderClosure
        fields = ['close_price', 'price_turi']


class AccountingSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)

    class Meta:
        model = Accounting
        fields = '__all__'
