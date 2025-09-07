from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # import the whole views module instead of just register

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(),
         name='library_detail'),

    # function-based register view (checker wants "views.register")
    path('register/', views.register, name='register'),

    # Django’s built-in authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
