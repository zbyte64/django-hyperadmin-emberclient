============
Introduction
============

django-hyperadmin-emberclient is a hyper admin client powered by emberjs.

--------
Features
--------
Defines it's own media type: application/vnd.Collection.hyperadmin.emberclient+JSON


------------
Requirements
------------

* Python 2.6 or later
* Django 1.3 or later
* django-hyperadmin


============
Installation
============

Put 'emberclient' into your ``INSTALLED_APPS`` section of your settings file.

And the following to urls.py::

    import hyperadmin
    from emberclient.clients import EmberJSClient
    admin_client = EmberJSClient(hyperadmin.site)

Add to root url patterns::

    url(r'^emberjs-admin/', include(admin_client.urls)),

