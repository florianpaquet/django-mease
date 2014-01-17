django-mease
============

Work in progress

Websocket integration made easy for Django using Tornado, Redis PUB/SUB and easy to use callback registry mechanism.

## Installation
### Dependencies (Debian & Ubuntu)
```
sudo apt-get install redis-server python-dev
```
### Install django-mease
```
pip install django-mease
```

### Add mease to your INSTALLED_APPS
```python
INSTALLED_APPS = (
  ...
  'mease',
)
```

## Usage
### Start websocket server
`python manage.py start_websocket_server`

### Register callbacks
Create `mease_registry.py` files to register your callbacks (the file must be located in an installed app):

```python
import mease

def receive_websocket_message(client, message, clients_list):
    for c in clients_list:
        c.write_message(message)

mease.receiver(receive_websocket_message)

def send_websocket_message(clients_list, channel, message):
    for c in clients_list:
        c.write_message(message)

mease.sender(send_websocket_message, channels=['websocket'])
```

Receiver functions are called when a message is sent from the client.

`mease.receiver` functions must take 3 parameters:

1. the client (tornado WebSocketHandler instance)
2. the message content
3. a list of all connected clients (list of tornado WebSocketHandler instances)

---

Sender functions are called when a message is sent from the server.

`mease.sender` functions must take 3 parameters:

1. a list of all connected clients (list of tornado WebSocketHandler instances)
2. the target channel
3. the message content

A sender function can be registered for a list of channels, otherwise it is registered for all channels.

### Publish
Use `mease.publish` to publish from anywhere in your code :
```python
import mease

mease.publish('websocket', "Hello world !")
```

This will call all sender functions registered on the 'websocket' channel.
