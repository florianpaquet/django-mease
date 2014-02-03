django-mease
============

Work in progress.

Websocket integration made easy for Django using Tornado, Redis PUB/SUB and easy to use callback registry mechanism.

See a full working example `here <https://github.com/florianpaquet/django-mease-example>`_

RTD INCOMING SHORTLY
--------------------

Installation
------------

Dependencies (Debian & Ubuntu)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Mease`` comes with Redis PUB/SUB backend by default. If you want to use it, install these dependencies :

::

    sudo apt-get install redis-server python-dev
    pip install redis


Install django-mease
~~~~~~~~~~~~~~~~~~~~

::

    pip install django-mease


Add mease to your INSTALLED_APPS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    INSTALLED_APPS = (
      # List of your installed apps
      'djmease',
    )



Usage
-----

Start websocket server
~~~~~~~~~~~~~~~~~~~~~~

``python manage.py run_websocket_server``


Register callbacks
~~~~~~~~~~~~~~~~~~

Create ``mease_registry.py`` files to register your callbacks (the file must be located in an installed app):

.. code:: python

    from djmease import mease

    @mease.opener
    def open_websocket(client, clients_list):
        client.storage["name"] = "mymane"
        for c in clients_list:
            c.send("Someone joined")

    @mease.closer
    def close_websocket(client, clients_list):
        for c in clients_list:
            c.send("{name} left".format(name=client.storage["name"]))

    @mease.receiver
    def receive_websocket_message(client, clients_list, message):
        for c in clients_list:
            c.send(message)

    @mease.sender(routing=['websocket'])
    def send_websocket_message(channel, clients_list, myobj):
        for c in clients_list:
            c.send(myobj.myattr)


Publish
~~~~~~~

Use ``mease.publish`` to publish from anywhere in your code :

.. code:: python

    from djmease import mease

    mease.publish('websocket', "Hello world !")


This will call all sender functions registered on the 'websocket' routing.
