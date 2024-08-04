from django.urls import path, include
from . import views 

urlpatterns = [
    # ... other URL patterns for membership app
    path('member/', include('membership.api.member.urls')), 
]
