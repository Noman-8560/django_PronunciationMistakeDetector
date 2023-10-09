from django.contrib import admin
from django.urls import path, include  # Import include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quickstart/', include('quickstart.urls')),  # Include app's URLs
    # Add more project-level URL patterns as needed
]
