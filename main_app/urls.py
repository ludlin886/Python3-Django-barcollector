from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bars/', views.bars_index, name='index'),
    path('bars/<int:bar_id>/', views.bars_detail, name='detail'),
    path('bars/create/', views.BarCreate.as_view(), name='bars_create'),
    path('bars/<int:pk>/update', views.BarUpdate.as_view(), name='bars_update'),
    path('bars/<int:pk>/delete', views.BarDelete.as_view(), name='bars_delete'),
]