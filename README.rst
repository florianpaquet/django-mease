django-mease
============

Work in progress

RTD INCOMING SHORTLY
--------------------

Websocket integration made easy for Django using Tornado, Redis PUB/SUB and easy to use callback registry mechanism.


Installation
------------

Dependencies (Debian & Ubuntu)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Mease`` comes with Redis PUB/SUB backend by default. If you want to use it, install these dependencies :

::

    sudo apt-get install redis-server python-dev
    pip install redis toredis-mease


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

    @mease.receiver
    def receive_websocket_message(client, message, clients_list):
        for c in clients_list:
            c.write_message(message)

    @mease.sender(routing=['websocket'])
    def send_websocket_message(channel, message, clients_list):
        for c in clients_list:
            c.write_message(message)


Receiver functions are called when a message is sent from the client.

``mease.receiver`` functions must take 3 parameters:

1. the client (tornado WebSocketHandler instance)
2. the message content
3. a list of all connected clients (list of tornado WebSocketHandler instances)

-------

Sender functions are called when a message is sent from the server.

``mease.sender`` functions must take 3 parameters:

1. a list of all connected clients (list of tornado WebSocketHandler instances)
2. the target routing
3. the message content

A sender function can be registered for a list of routings, otherwise it is registered globally.


Publish
~~~~~~~

Use ``mease.publish`` to publish from anywhere in your code :

.. code:: python

    from djmease import mease

    mease.publish('websocket', "Hello world !")


This will call all sender functions registered on the 'websocket' routing.
