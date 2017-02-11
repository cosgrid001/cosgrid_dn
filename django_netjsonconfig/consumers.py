import logging
from channels import Group
from channels.sessions import channel_session

log = logging.getLogger(__name__)


@channel_session
def ws_connect(message):
    paths = message['path'].decode('ascii').strip('/').split('/')
    if len(paths) != 1:
        return
    label = paths[0]
    Group(label, channel_layer=message.channel_layer).add(message.reply_channel)
    Group(label).send({'text': 'connected'})
    message.channel_session['label'] = label

@channel_session
def ws_receive(message):
    label = message.channel_session['label']
    data = message['text']
    Group(label, channel_layer=message.channel_layer).send({'text': data})


@channel_session
def ws_disconnect(message):
    label = message.channel_session['label']
    Group(label, channel_layer=message.channel_layer).discard(message.reply_channel)
