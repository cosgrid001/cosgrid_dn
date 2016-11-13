
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django_netjsonconfig.models import vpn
from django_netjsonconfig.models import config
from django_netjsonconfig.models import template
from django_x509.models import Ca, Cert
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class VpnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vpn.Vpn
        fields = '__all__'

class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = config.Config
        fields = '__all__'

class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = template.Template
        fields = '__all__'

class CaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ca
        fields = '__all__'

class CertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cert
        fields = '__all__'


