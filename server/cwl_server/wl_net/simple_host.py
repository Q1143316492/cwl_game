import cwl_server.wl_net.net_conf as conf
import socket


class SimpleHost(object):

    def __init__(self, timeout=conf.NET_HOST_DEFAULT_TIMEOUT):
        self.sock = None
        self.port = 7736
        self.state = conf.NET_STATE_STOP

    def start(self, port=7736):
        self.stop()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.sock.bind(('0.0.0.0', port))
        except IOError as e:
            try:
                self.sock.close()
            except IOError, e:
                pass  # should logging here
            return -1

        self.sock.listen(conf.MAX_HOST_CLIENTS_INDEX + 1)
        self.sock.setblocking(False)
        self.port = self.sock.getsockname()[1]
        self.state = conf.NET_STATE_ESTABLISHED

    def stop(self):
        pass
