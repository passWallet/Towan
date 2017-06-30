from channels.routing import route, include
from towan.consumers import basic_connect, basic_disconnect, client_connect, client_disconnect

basic_routing = [
    route("websocket.connect", basic_connect),
    route("websocket.disconnect", basic_disconnect)
]

client_routing = [
    route("websocket.connect", client_connect),
    route("websocket.disconnect", client_disconnect)
]

routing = [
    include(client_routing, path=r"^/client"),
    include(basic_routing),
]
