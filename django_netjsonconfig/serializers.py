
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
        fields = ("id", "url", "username", "email", "groups")

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "url", "name")

class VpnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vpn.Vpn
        fields = ("id", "url", "name", "host", "backend", "ca", "cert", "notes")

class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = config.Config
        fields = ("id", "url", "name", "backend", "config", "created", "modified", "status", "key",
                  "mac_address", "last_ip", "templates", "vpn")

class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = template.Template
        fields = ("id", "url", "name", "backend", "config", "created", "modified", "type", "default", "auto_cert", "vpn")

class CaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ca
        fields = ("id", "url", "name", "notes", "key_length", "digest", "validity_start", "validity_end",
                  "country_code", "state", "city", "organization", "email", "common_name", "extensions",
                  "serial_number", "certificate", "private_key", "created", "modified")

class CertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cert
        fields = ("id", "url", "name", "notes", "key_length", "digest", "validity_start", "validity_end",
                  "country_code", "state", "city", "organization", "email", "common_name", "extensions",
                  "serial_number", "certificate", "private_key", "created", "modified", "revoked", "revoked_at", "ca")


