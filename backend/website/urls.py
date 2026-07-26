from django.urls import path
from .views import homepage_data, create_lead, blog_list, blog_detail

urlpatterns = [
    path('homepage/', homepage_data, name='homepage-data'),
    path('lead/', create_lead, name='create-lead'),
    path('blog/', blog_list, name='blog-list'),
    path('blog/<slug:slug>/', blog_detail, name='blog-detail'),
]
