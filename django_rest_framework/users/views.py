from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from .models import CustomUser as user


# Create your views here.
class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request.data) # JSON Type 임

        # JSON을 Object로 어떻게 바꿀것인가?
        user_serializer = UserSerializer(data = request.data) # instance로 넘겨줘야 할때도 있고, data로 넘겨줘야 할 때도 있다.
        # JSON -> Object
        # data(JSON -> OBJ), instance(OBJ -> JSON)

        if (user_serializer.is_valid()):
            #이런식으로 해두면 받은 정보를 저장한다
            saved_user = user_serializer.save()
            print("saved_user =",saved_user)
            return Response(
                {
                    'your user' : user_serializer.data,
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                'errors':user_serializer.errors,
                'message': "예외처리 한거",
            }, status=status.HTTP_400_BAD_REQUEST
        )
    
class DetailView(APIView):
    def get(self, request, pk):
        user_data = user.objects.get(user_id=pk) # serializer 돌릴때는 get으로 해줘야된다
        user_serializer = UserSerializer(user_data)
        #user_serializer = UserSerializer(user_data, many=True) # 오브젝트가 여러개인 쿼리셋을 리턴해주고싶다? 하면 이걸돌리면된다~~~

        return Response(user_serializer.data, status=status.HTTP_200_OK)
