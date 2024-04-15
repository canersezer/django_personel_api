from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Departman,Person
from .seriliazers import DepartmanSerializer,PersonSerializer
from .permissions import IsAdminOrReadOnly


class DepartmanMVS(viewsets.ModelViewSet):
    queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer
    permission_classes = [IsAdminOrReadOnly,IsAuthenticated]


class PersonMVS(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAdminOrReadOnly,IsAuthenticated]


@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"detail":"User Logout"})

