from django.http import JsonResponse
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .forms import SignUpForm
from .models import User


class SignupAPIView(APIView):
    """Регистрация"""
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        data = request.data
        message = 'success'
        form = SignUpForm({
            'email': data.get('email'),
            'username': data.get('username'),
            'password1': data.get('password1'),
            'password2': data.get('password2'),
        })

        if form.is_valid():
            form.save()
        else:
            message = form.errors.as_json()

        return JsonResponse({'message': message}, safe=False)


@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,

    })



