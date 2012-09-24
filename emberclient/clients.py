from hyperadmin.clients.common import SimpleTemplateClient

from emberclient.mediatypes import CollectionEmberClientJSON

class EmberJSClient(SimpleTemplateClient):
    template_name = 'emberclient/index.html'
    
    def __init__(self, *args, **kwargs):
        super(EmberJSClient, self).__init__(*args, **kwargs)
        if hasattr(self.api_endpoint, 'register_media_type'):
            self.api_endpoint.register_media_type(CollectionEmberClientJSON, 'application/vnd.Collection.hyperadmin.emberclient+JSON')

