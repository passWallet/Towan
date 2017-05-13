from channels.routing import route
from towan.consumers import ws_connect, ws_disconnect

channel_routing = [
    route("websocket.connect", ws_connect, path=r"^/(?P<address>[a-zA-Z0-9_]+)/$"),
    route("websocket.disconnect", ws_disconnect)
]
