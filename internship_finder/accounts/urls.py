from django.urls import path, include

from internship_finder.accounts.views import StudentRegistrationAPIView, CompanyRegistrationAPIView

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('register_student/', StudentRegistrationAPIView.as_view(), name='register_student'),
    path('register_company/', CompanyRegistrationAPIView.as_view(), name='register_company')
]