from rest_framework import serializers

from .models import CustomUser as User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # 무슨 모델을 쓸지
        # fields = ['username', 'password', 'firstname']# 이렇게 어떤 부분만 직렬화 할지 고를수 있다.
        fields = '__all__'
        # extra_kwargs = {"password": {'write_only': True}} # 이런식으로 이것만 빼고! 도 지정할 수 있다.

    # 이안에 검사 메소드 몇가지를 더 구현해 줄수도 있다.
    # def create()