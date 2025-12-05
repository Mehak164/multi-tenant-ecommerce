from rest_framework import serializers
from django.contrib.auth import get_user_model
from tenants.models import Tenant
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    tenant_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role', 'tenant_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        tenant_name = validated_data.pop('tenant_name')
        email = validated_data.get('email', '')

        tenant, created = Tenant.objects.get_or_create(
            name=tenant_name,
            defaults={
                'domain': f'{tenant_name}.com',
                'contact_email': email
            }
        )

        if not created and not tenant.contact_email:
            tenant.contact_email = email
            tenant.save()

        user = User.objects.create_user(**validated_data, tenant=tenant)
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['tenant_id'] = user.tenant.id if user.tenant else None
        token['role'] = user.role
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['tenant_id'] = self.user.tenant.id if self.user.tenant else None
        data['role'] = self.user.role
        return data
