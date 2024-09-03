from django_filters import rest_framework as filters
from .models import KOrder

class OrdersFilter(filters.FilterSet):
    class Meta:
        model = KOrder
        fields = ('id','status','payment_status','payment_mode')



