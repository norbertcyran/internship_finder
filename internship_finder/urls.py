"""internship_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .accounts.views import UserViewSet
from .announcements.views import AnnouncementViewSet, ApplicationViewSet
from .companies.views import CompanyViewSet, OfficeViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'users', UserViewSet)

companies_router = NestedSimpleRouter(router, r'companies', lookup='company')
companies_router.register(r'offices', OfficeViewSet, base_name='company-offices')

announcements_router = NestedSimpleRouter(router, r'announcements', lookup='announcement')
announcements_router.register(r'applications', ApplicationViewSet, base_name='announcement-applications')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(companies_router.urls)),
    path('api/', include(announcements_router.urls)),
    path('api/auth/', include('rest_auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
