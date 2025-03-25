from sqlite3 import IntegrityError

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView

from users.models import Role, CustomUser
from users.serializers import UserSerializer


class CheckStatusView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'message': 'success'}, status=HTTP_200_OK)

class AllUsersView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        users = CustomUser.objects.all()
        users_serialized = UserSerializer(users, many=True)
        return Response (users_serialized.data, status=HTTP_200_OK)

class GetUserByEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        user = CustomUser.objects.filter(email=email).values("id", "email").first()
        return Response({"users": user}, status=HTTP_200_OK)

class GetUserByRoleView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        role_name = request.data.get('role')
        user = CustomUser.objects.filter(role__name__iexact =role_name).values("id", "email", "role__name").all()
        return Response({"users": user}, status=HTTP_200_OK)

class GetUserByRoleSlugView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug):
        user = CustomUser.objects.filter(role__slug=slug).values("id", "email", "role__name").all()
        return Response({"users": user}, status=HTTP_200_OK)

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role')
        is_active = request.data.get('is_active', True)
        is_staff = request.data.get('is_staff', False)
        is_superuser = request.data.get('is_superuser', False)

        if not email or not password or not role:
            return Response(
                {"error": "Please fill all fields"},
                status=HTTP_400_BAD_REQUEST
            )

        if CustomUser.objects.filter(email=email).exists():
            return Response(
                {"error": "User already exists"},
                status=HTTP_400_BAD_REQUEST
            )

        if not Role.objects.filter(name__iexact = role).exists():
            return Response(
                {"error": "Role doesn't exist"},
                status=HTTP_400_BAD_REQUEST
            )

        try:
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                role=Role.objects.get(name=role),
                is_active=is_active,
                is_staff=is_staff,
                is_superuser=is_superuser,
            )
            user.save()
            return Response({"message": "User created correctly"}, status=HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"error: {e}"},
                status=HTTP_500_INTERNAL_SERVER_ERROR
            )

