from rest_framework import viewsets

from .models import Company, Office

from .serializers import CompanySerializer, OfficeSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class OfficeViewSet(viewsets.ModelViewSet):
    serializer_class = OfficeSerializer

    def get_queryset(self):
        return Office.objects.filter(company=self.kwargs['company_pk'])

    def perform_create(self, serializer):
        company = Company.objects.get(pk=self.kwargs['company_pk'])
        serializer.save(company=company)
