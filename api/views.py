from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterUserSerializer, LoginSerializer, OrderSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from orders.models import Orders
from products.models import Products
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message":"Registeration successfully", "user":serializer.data}, status=201)

@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == "POST":
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                print("Authenticated")
                # Generate a token for the frontend to use
                token, created = Token.objects.get_or_create(user=user)
                # refresh = RefreshToken.for_user(user)
        #         return Response({"Message":"user successfully logged in", "data":serializer.data, 'refresh': str(refresh),
        # # 'access': str(refresh.access_token)}, status=201)
                return Response({"Message":"user successfully logged in", "data":serializer.data, 'token':token.key}, status=201)
            # else:
            #     print("Not authenticated") 
            #     raise ValueError("User not authenticated")   
        else:
            return Response({"message":"not valida"})
    else:
        return Response({"data": "Later"})

class OrderViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer


class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


    
