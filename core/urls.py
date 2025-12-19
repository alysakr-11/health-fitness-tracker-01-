from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tracker.urls')),            # includes tracker app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout URLs
    path('admin/', admin.site.urls),
]
path('accounts/',include('django.contrib.auth.urls')),
