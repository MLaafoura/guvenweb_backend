from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fieldds = ('id', 'email', 'fullName', 'password', 'phone_number', 'is_admin',
                   'is_cyber_expert', 'is_client')
        