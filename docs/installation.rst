Installation
************

Dependencies
------------

``django-mease`` uses `Redis <http://redis.io/>`_ `PUB/SUB <http://redis.io/topics/pubsub>`_ to publish messages asynchronously between Django and Tornado WebSocket server.

Debian/Ubuntu::

    sudo apt-get install redis-server python-dev


Install using pip
-----------------

Install the latest stable release using pip::

    pip install django-mease


Add ``django-mease`` to your installed apps
-------------------------------------------

Enable ``django-mease`` by adding ``mease`` to `settings.INSTALLED_APPS <https://docs.djangoproject.com/en/1.6/ref/settings/#installed-apps>`_::

    INSTALLED_APPS = (
        # [...] Your list of installed apps
        'mease',
    )
