from django.conf.urls import patterns, url,include

urlpatterns = patterns(
    '',
    url(r'home/', 'logger.views.index'),
    url(r'^add/', 'logger.views.get_data'),
    )
