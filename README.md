django-mease
============

Websocket integration made easy for Django using Redis PUB/SUB and easy to use callback registry mechanism.

## Installation
### Dependencies (Debian & Ubuntu)
```
sudo apt-get install redis-server python-dev
```
### Install django-mease
```
python setup.py install
```

### Add mease to your INSTALLED_APPS
```python
INSTALLED_APPS = (
  ...
  'mease',
)
```

## Usage
### Register callbacks
