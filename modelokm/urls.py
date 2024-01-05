from django.urls import path
from modelokm.views import processing
from django.contrib import admin


urlpatterns=[
    path('admin/', admin.site.urls),
    path('', processing)
]