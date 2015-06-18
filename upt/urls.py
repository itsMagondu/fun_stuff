from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


from rest_framework import routers

from logger.views import DeviceViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)

urlpatterns = patterns(
    '',
    # Examples:
        # url(r'^$', 'upande_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^logger/', include('logger.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',name="up_login"),
    url(r'^', include(router.urls)),
     )
