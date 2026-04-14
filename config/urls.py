from django.urls import path
from django.contrib import admin

admin_site = admin.site

urlpatterns = [
    path("admin/", admin_site.urls),
]
