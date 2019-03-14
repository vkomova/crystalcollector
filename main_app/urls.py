from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crystals/', views.crystals_index, name='index'),
    path('crystals/<int:crystal_id>/', views.crystals_detail, name='detail'),
    path('crystals/create/', views.CrystalCreate.as_view(), name='crystals_create'),
    path('crystals/<int:pk>/update/', views.CrystalUpdate.as_view(), name='crystals_update'),
    path('crystals/<int:pk>/delete/', views.CrystalDelete.as_view(), name='crystals_delete'),
    path('crystals/<int:crystal_id>/add_uses/', views.add_uses, name='add_uses'),
    path('crystals/<int:crystal_id>/assoc_country/<int:country_id>/', views.assoc_country, name='assoc_country'),
    path('crystals/<int:crystal_id>/unassoc_country/<int:country_id>/', views.unassoc_country, name='unassoc_country'),
    path('countries/', views.CountryList.as_view(), name='countries_index'),
    path('countries/<int:pk>/', views.CountryDetail.as_view(), name='countries_detail'),
    path('countries/create/', views.CountryCreate.as_view(), name='countries_create'),
    path('countries/<int:pk>/update/', views.CountryUpdate.as_view(), name='countries_update'),
    path('countries/<int:pk>/delete/', views.CountryDelete.as_view(), name='countries_delete'),
    path('crystals/<int:crystal_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]
