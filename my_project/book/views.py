
from rest_framework import viewsets
from . import models
from . import serializers
from .serializers import ProductSerializer,CategorySerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
     
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)















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


