from django.conf.urls.defaults import patterns, include, url
import hyperadmin
from emberclient.clients import EmberJSClient

admin_client = EmberJSClient(api_endpoint=hyperadmin.site)

urlpatterns = patterns('',
    url(r'^', include(admin_client.urls)),
)

