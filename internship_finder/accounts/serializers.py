from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'full_name',
            'date_joined',
            'is_active',
            'is_staff',
            'is_superuser',
        )

        read_only_fields = ('email', 'is_staff', 'is_superuser', 'date_joined')
