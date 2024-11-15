

from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("warmup-2/front-times", warmup_2),
    path("logic-2/no-teen-sum", logic_2),
    path("string-2/xyz_there", string_2),
    path("list-2/centered-average", list_2),
]