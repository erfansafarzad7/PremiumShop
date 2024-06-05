from django.urls import path,include
from . import views

app_name = "items"

urlpatterns = [
    path('all-items/',views.ItemsView.as_view(),name="all_items"),
    path('detail/<str:title>/',views.ItemDetailView.as_view(),name="detail"),
    path('<str:title>/',views.CategoryFilterView.as_view(),name="category_filter"),

]
