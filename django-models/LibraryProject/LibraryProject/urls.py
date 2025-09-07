from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirect root URL to /books/ (so visiting http://127.0.0.1:8000/ works)
    path('', lambda request: redirect('list_books')),

    # Include your app URLs
    path('', include('relationship_app.urls')),
]
