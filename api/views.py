from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([AllowAny])
def public_endpoint(request):
    return Response({"message": "This is a public endpoint"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_endpoint(request):
    return Response({"message": "This is a protected endpoint", "user": request.user.username})

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({"error": "Username and password required"}, status=400)
    
    user = User.objects.create_user(username=username, password=password)
    token = Token.objects.create(user=user)
    return Response({"token": token.key, "user_id": user.id})
