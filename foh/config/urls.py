from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path("hey-name", hey_name),
    path("age-in", age_in),
    path("order", order),
]


