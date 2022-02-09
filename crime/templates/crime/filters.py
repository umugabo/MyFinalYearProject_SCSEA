import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class SuspectFilter(django_filters.FilterSet):
	f_name = DateFilter(field_name="date_created", lookup_expr='gte')
	arrest_date = DateFilter(field_name="date_arrested", lookup_expr='lte')
	gender = CharFilter(field_name='gender', lookup_expr='icontains')


	class Meta:
		model = Suspect
		fields = '__all__'
