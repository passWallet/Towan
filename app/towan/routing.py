from channels.routing import route
from towan.consumers import ws_connect, ws_disconnect

channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.disconnect", ws_disconnect)
]
