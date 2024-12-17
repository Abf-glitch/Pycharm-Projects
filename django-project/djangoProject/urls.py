from django.contrib import admin
from django.urls import path
# imported views
from djangoProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # configured the url
    path('', views.index, name='index'),
]
