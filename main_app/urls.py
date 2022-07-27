from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bars/', views.bars_index, name='index'),
    path('bars/<int:bar_id>/', views.bars_detail, name='detail'),
    path('bars/create/', views.BarCreate.as_view(), name='bars_create'),
    path('bars/<int:pk>/update', views.BarUpdate.as_view(), name='bars_update'),
    path('bars/<int:pk>/delete', views.BarDelete.as_view(), name='bars_delete'),
    path('bars/<int:bar_id>/add_rating/', views.add_rating, name='add_rating'),
    path('avaliable/', views.AvaliableList.as_view(), name='avaliable_index'),
    path('avaliable/<int:pk>/', views.AvailableDetail.as_view(), name='avaliable_detail'),
    path('avaliable/create/', views.AvaliableCreate.as_view(), name='avaliable_create'),
    path('avaliable/<int:pk>/update/', views.AvaliableUpdate.as_view(), name='avaliable_Update'),
    path('avaliable/<int:pk>/delete/', views.AvaliableDelete.as_view(), name='avaliable_delete'),
    path('bars/<int:bar_id>/assoc_bar/<int:avaliable_id>/', views.assoc_avaliable, name='assoc_avaliable'),
]