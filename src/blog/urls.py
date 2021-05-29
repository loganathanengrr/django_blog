from django.urls import path

from .views import (
        blog_detail_page,
        blog_list_page,
        blog_create_view,
        blog_update_view,
        blog_delete_view
        )

urlpatterns = [
        path('', blog_list_page),
        path('<slug:slug>/', blog_detail_page),
        path('<slug:slug>/edit/', blog_update_view),
        path('<slug:slug>/delete/', blog_delete_view),   
    ]