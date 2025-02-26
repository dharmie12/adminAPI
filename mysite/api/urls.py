"""from django.urls import path
from . import views


urlpatterns = [
    path("blogposts/", views.BLogPostListCreate.as_view(), name="create-new-blogpost"),
    
]"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),  # Link to app URLs
]



