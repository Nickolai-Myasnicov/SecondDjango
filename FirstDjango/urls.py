from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main),
    path('about/', views.about),
    path('item/<int:id>/', views.show_item, name="item-page"),
    path('items/', views.items_list),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
