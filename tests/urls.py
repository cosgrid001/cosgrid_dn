from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from django_netjsonconfig import views

admin.autodiscover()


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'vpns', views.VpnViewSet)
router.register(r'configs', views.ConfigViewSet)
router.register(r'templates', views.TemplateViewSet)
router.register(r'cas', views.CaViewSet)
router.register(r'certs', views.CertViewSet)


urlpatterns = [
    url(r'config', views.ConfigView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    # controller URLs
    # used by devices to download/update their configuration
    # keep the namespace argument unchanged
    url(r'^', include('django_netjsonconfig.controller.urls', namespace='controller')),
    # common URLs
    # shared among django-netjsonconfig components
    # keep the namespace argument unchanged
    url(r'^', include('django_netjsonconfig.urls', namespace='netjsonconfig')),
    url(r'^', include('django_x509.urls', namespace='x509')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += staticfiles_urlpatterns()

