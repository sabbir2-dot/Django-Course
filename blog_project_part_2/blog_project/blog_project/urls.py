from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('category/<slug:category_slug>/', views.home, name='category_wise_post'),
    path('author/', include('author.urls')),
    path('post/', include('posts.urls')),
    path('category/', include('categories.urls')),

]
