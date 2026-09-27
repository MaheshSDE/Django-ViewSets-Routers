# from django.urls import path
# from .views import ProductListView, ProductDetailView

# urlpatterns = [
#     path('products/',          ProductListView.as_view(),   name='product-list'),
#     path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
# ]


from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router= DefaultRouter()
router.register('products',ProductViewSet)

urlpatterns=router.urls