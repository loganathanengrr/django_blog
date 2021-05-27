from django.urls import path

from .views import (
        blog_detail_page,
        blog_list_page,
        blog_create_view
        )

urlpatterns = [
        path('', blog_list_page),
        path('<slug:slug>/', blog_detail_page),
        path('create/', blog_create_view),
    ]