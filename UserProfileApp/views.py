from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .renderers import UserJSONRenderer
from .serializers import (LoginSerializer, RegistrationSerializer, UserDataSerializer)


class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        # user = request.data.get('user', {})
        serializer_data = {}
        for i, item in enumerate(request.data):
            data = request.data.get(item, None)
            if data is not None:
                serializer_data.update({f'{item}': data})
        # Паттерн создания сериализатора, валидации и сохранения - довольно
        # стандартный, и его можно часто увидеть в реальных проектах.
        print(serializer_data)
        serializer = self.serializer_class(data=serializer_data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer_data = {}
        for i, item in enumerate(request.data):
            data = request.data.get(item, None)
            if data is not None:
                serializer_data.update({f'{item}': data})
        serializer = self.serializer_class(data=serializer_data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDataAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserDataSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data={'user': request.user}, partial=True,
                                           context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
