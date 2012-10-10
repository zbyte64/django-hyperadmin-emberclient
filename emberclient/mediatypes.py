from hyperadmin.mediatypes.collectionjson import CollectionHyperAdminJSON

class CollectionEmberClientJSON(CollectionHyperAdminJSON):
    recognized_media_types = [
        'application/vnd.Collection.hyperadmin.emberclient+JSON'
    ]

