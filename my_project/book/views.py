
from rest_framework import viewsets
from . import models
from . import serializers
from .serializers import ProductSerializer,CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    
     
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer





























# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (permissions.AllowAny,)
    

# class Create(generics.CreateAPIView):
#     model = Product
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (permissions.AllowAny,)

# class Update(generics.RetrieveUpdateDestroyAPIView):
#     model = Product
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (permissions.AllowAny,)
#     # template_name = 'update_product.html'
#     # fields = '__all__'

# class Remove(DeleteView):
#     model = Product
#     template_name = 'remove_product.html'
#     success_url = 'home'

        
# class List(ListView):
#     model = Product
#     template_name = 'home.html'

# class Detail(DetailView):
#     model = Product
#     template_name = 'product_detail.html'


